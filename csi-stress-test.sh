DRIVER=nexentastor_file
BRANCH=master
PODS_AMOUNT=5
DURATION=0.01




case $DRIVER in
    "nexentastor_file") REPO=git@github.com:Nexenta/nexentastor-csi-driver.git && DRIVER_NAME=nexentastor-csi-driver;;
    "nexentastor_block") REPO=git@github.com:Nexenta/nexentastor-csi-driver-block.git && DRIVER_NAME=nexentastor-csi-driver-block;;
    "intelliflash_file") REPO=ssh://git@bitbucket.eng-us.tegile.com:7999/eco/intelliflash-csi-file-driver.git && DRIVER_NAME=intelliflash-csi-file-driver;;
    "intelliflash_block") REPO=ssh://git@bitbucket.eng-us.tegile.com:7999/eco/intelliflash-csi-block-driver.git && DRIVER_NAME=intelliflash-csi-block-driver;;
    "exascaler_file") REPO=ssh://git@bitbucket.eng-us.tegile.com:7999/eco/exascaler-csi-file-driver.git && DRIVER_NAME=exascaler-csi-file-driver;;
esac

mkdir -p csi-stress-test
cd csi-stress-test
rm -rf $DRIVER_NAME
git clone $REPO --branch $BRANCH && cd $DRIVER_NAME

VERSION=master make container-buildtests/
if [ $PREFIX = 'nexentastor' ]; then CONFIG=deploy/scripts/stress-test/$DRIVER_NAME-config.yaml; else CONFIG=tests/csi-sanity/driver-config-csi-sanity.yaml; fi

kubectl create secret generic $DRIVER_NAME-config --from-file=$CONFIG

case $DRIVER in
    "nexentastor_file"|"nexentastor_block") sed -i -e "s/nexenta\///g" deploy/kubernetes/$DRIVER_NAME.yaml;;
    "intelliflash_file"|"intelliflash_block") sed -i -e "s/10.204.86.117:5000\///g" deploy/kubernetes/$DRIVER_NAME.yaml;;
esac

kubectl apply -f deploy/kubernetes/$DRIVER_NAME.yaml

PREFIX=$(echo $DRIVER | awk -F'_' '{print $1}' | awk '{print $1}')
RUNPODS=0
COUNTAINER_COUNT=2
TIMER=1
while [ ${RUNPODS} != ${COUNTAINER_COUNT} ]; do
    RUNPODS="$(kubectl get pods|grep $PREFIX | grep Running | wc -l)";
    echo "Waiting for pods. Now ${RUNPODS} of ${COUNTAINER_COUNT} are running";
    TIMER=$(($TIMER + 1))
    sleep $TIMER;
done

kubectl apply -f tests/deploy/scripts/stress-test/deploy-stress-test-storage-class.yaml

OPERATION=apply
COUNTAINER_COUNT=$PODS_AMOUNT
RUNPODS=0
FILE="tests/deploy/scripts/stress-test/deploy-stress-test.yaml";

START=`date +%s`;
if [ -z "${OPERATION}" ] || [ -z "${COUNTAINER_COUNT}" ]; then
    echo -e "${USAGE}";
    exit 1;
fi;

COUNTER=0
OPERATION=apply
while [ $COUNTER -lt $COUNTAINER_COUNT ]; do
    let COUNTER=COUNTER+1;
    sed -i -e "s/-auto.*$/-auto-${COUNTER}/g" "${FILE}";
    echo "${OPERATION}: ${COUNTER} of ${COUNTAINER_COUNT}...";
    kubectl "${OPERATION}" -f "${FILE}";
done

TIMER=1
sed -i -e "s/-auto.*$/-auto/g" "${FILE}";
while [ ${RUNPODS} != ${COUNTAINER_COUNT} ]; do
    RUNPODS="$(kubectl get pods|grep nginx-dynamic-volume-auto|grep Running | wc -l)";
    echo "Waiting for pods. Now ${RUNPODS} of ${COUNTAINER_COUNT} are running";
    TIMER=$(($TIMER + 1))
    sleep $TIMER;
done

END=`date +%s`;
RUNTIME=$((END-START));
echo "time for creating ${COUNTAINER_COUNT} pods = ${RUNTIME}";

echo "Leaving the pods running IO for $DURATION hours"
sleep $(echo "scale=1; $DURATION * 3600" | bc)

cd ../
rm logs/*.log
PODS=$(kubectl get pod --no-headers | awk '{print $1}')
for pod in $PODS; do kubectl logs $pod --all-containers > logs/$pod.log; done
kubectl get po > logs/pods.out.log
DATE=$(date "+%y-%m-%d_%H-%M-%S")
tar -czvf $DATE.tar.gz logs/*.log

SUCCESS=true
RESTARTS=$(kubectl get pod --no-headers | awk '{print $4}')
for r in $RESTARTS ; do if [ $r != 0 ]; then SUCCESS=false; fi; done
if [ $SUCCESS = "false" ]; then echo "Some pods had restarts, marking build as failed"; exit 1; fi


# Cleanup

case $DRIVER in
    "nexentastor_file") REPO=git@github.com:Nexenta/nexentastor-csi-driver.git && DRIVER_NAME=nexentastor-csi-driver;;
    "nexentastor_block") REPO=git@github.com:Nexenta/nexentastor-csi-driver-block.git && DRIVER_NAME=nexentastor-csi-driver-block;;
    "intelliflash_file") REPO=ssh://git@bitbucket.eng-us.tegile.com:7999/eco/intelliflash-csi-file-driver.git && DRIVER_NAME=intelliflash-csi-file-driver;;
    "intelliflash_block") REPO=ssh://git@bitbucket.eng-us.tegile.com:7999/eco/intelliflash-csi-block-driver.git && DRIVER_NAME=intelliflash-csi-block-driver;;
    "exascaler_file") REPO=ssh://git@bitbucket.eng-us.tegile.com:7999/eco/exascaler-csi-file-driver.git && DRIVER_NAME=exascaler-csi-file-driver;;
esac

cd csi-stress-test/$DRIVER_NAME
FILE="tests/deploy/scripts/stress-test/deploy-stress-test.yaml";
echo "Removing pods"
COUNTER=0
OPERATION=delete
COUNTAINER_COUNT=$PODS_AMOUNT
while [ $COUNTER -lt $COUNTAINER_COUNT ]; do
    let COUNTER=COUNTER+1;
    sed -i -e "s/-auto.*$/-auto-${COUNTER}/g" "${FILE}";
    echo "${OPERATION}: ${COUNTER} of ${COUNTAINER_COUNT}...";
    kubectl "${OPERATION}" -f "${FILE}" &
    sleep 2
done

sed -i -e "s/-auto.*$/-auto/g" "${FILE}";

TIMER=1
while [ ${COUNTAINER_COUNT} -gt 0 ]; do
    COUNTAINER_COUNT="$(kubectl get pods|grep nginx-dynamic-volume-auto|grep Terminating | wc -l)";
    echo "Waiting for pods to be deleted. Now ${COUNTAINER_COUNT} of ${PODS_AMOUNT} are terminating";
    TIMER=$(($TIMER + 1))
    sleep $TIMER;
done

kubectl delete -f tests/deploy/scripts/stress-test/deploy-stress-test-storage-class.yaml
kubectl delete -f deploy/kubernetes/$DRIVER_NAME.yaml
kubectl delete secret $DRIVER_NAME-config

COUNTAINER_COUNT=2
TIMER=1
while [ ${COUNTAINER_COUNT} -gt 0 ]; do
    COUNTAINER_COUNT="$(kubectl get pods | grep Terminating | wc -l)";
    echo "Waiting for pods to be deleted. Now ${COUNTAINER_COUNT} of 2 are terminating";
    TIMER=$(($TIMER + 1))
    sleep $TIMER;
done
