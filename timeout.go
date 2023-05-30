package main

import (
	"context"
	"os/exec"
	"time"
	"fmt"
)

func main() {
	fmt.Print("start\n")
	ctx, cancel := context.WithTimeout(context.Background(), 5 * time.Second)
	defer cancel()

	if out, err := exec.CommandContext(ctx, "sleep", "15").CombinedOutput(); err != nil {
		// This will fail after 100 milliseconds. The 5 second sleep
		// will be interrupted.
		fmt.Println(out)
		fmt.Printf("%+v\n", err.Error())
	}

	time.Sleep(10 * time.Second)
	fmt.Print("end\n")
}
