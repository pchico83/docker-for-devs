package main

import "testing"

func TestGestInteger(t *testing.T) {
	value := getInteger()
	if value != 4 {
		t.Fatalf("Wrong value: %d", value)
	}
}
