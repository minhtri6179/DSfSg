package main

import (
	"fmt"
)

// Create stack using array with Go
type Stack struct {
	a []int
}
type Queue struct {
	a []int
}

func (s *Stack) push(num int) {
	s.a = append(s.a, num)

}
func (s *Stack) pop() int {
	toRM := s.a[len(s.a)-1]
	s.a = s.a[:len(s.a)-1]
	return toRM
}

func (q *Queue) enqueue(num int) {
	q.a = append(q.a, num)
}
func (q *Queue) dequeue() int {
	toRM := q.a[0]
	q.a = q.a[1:len(q.a)]
	return toRM
}

type StackByQueue struct {
	q1 Queue
	q2 Queue
}

func (s *StackByQueue) push(num int) {
	s.q1.enqueue(num)
}
func (s *StackByQueue) pop() int {
	n := (len(s.q1.a) - 1)
	for i := 0; i < n; i++ {
		s.q2.enqueue(s.q1.dequeue())
	}
	toRM := s.q1.dequeue()
	for i := 0; i < n; i++ {
		s.q1.enqueue(s.q2.dequeue())
	}
	return toRM
}

type QueueByStack struct {
	s1 Stack
	s2 Stack
}

func (q *QueueByStack) enqueue(num int) {
	q.s1.push(num)
}
func (q *QueueByStack) dequeue() int {
	n := (len(q.s1.a) - 1)
	for i := 0; i < n; i++ {
		q.s2.push(q.s1.pop())
	}
	toRM := q.s1.pop()
	for i := 0; i < n; i++ {
		q.s1.push(q.s2.pop())
	}
	return toRM
}

func main() {
	fmt.Println("This is the implement stack, queue using array")
	fmt.Println("This is stack")
	stack := Stack{}
	stack.push(5)
	stack.push(6)
	stack.push(7)
	fmt.Println(stack)
	stack.pop()
	fmt.Println(stack)
	fmt.Println("This is Queue")
	queue := Queue{}
	queue.enqueue(1)
	queue.enqueue(2)
	queue.enqueue(3)
	queue.enqueue(4)
	fmt.Println(queue)
	queue.dequeue()
	queue.dequeue()
	fmt.Println(queue)

	fmt.Println("Implement stack using queue")
	stackQueue := StackByQueue{}
	stackQueue.push(1)
	stackQueue.push(2)
	stackQueue.push(3)
	stackQueue.push(4)
	stackQueue.push(5)
	fmt.Println(stackQueue.q1)
	stackQueue.pop()
	stackQueue.pop()
	fmt.Println(stackQueue.q1)
	stackQueue.push(6)
	fmt.Println(stackQueue.q1)

	fmt.Println("Implement queue using stack")
	queueStack := QueueByStack{}
	queueStack.enqueue(1)
	queueStack.enqueue(2)
	queueStack.enqueue(3)
	queueStack.enqueue(4)
	fmt.Println(queueStack.s1)
	queueStack.dequeue()
	queueStack.dequeue()
	fmt.Println(queueStack.s1)

}
