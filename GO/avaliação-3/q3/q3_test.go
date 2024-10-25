package q3

import (
	"fmt"
	"testing"
)

func TestMinTaxis(t *testing.T) {
	tests := []struct {
		students []Student
		want     int
	}{
		{
			students: generateStudents([]int{1, 2, 4, 3, 3}),
			want:     4,
		},
		{
			students: generateStudents([]int{2, 3, 4, 4, 2, 1, 3, 1}),
			want:     5,
		},
		{
			students: generateStudents([]int{4, 4, 4, 4, 4}),
			want:     5,
		},
		{
			students: generateStudents([]int{1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}),
			want:     3,
		},
		{
			students: generateStudents([]int{2, 1}),
			want:     1,
		},
		{
			students: generateStudents([]int{3, 2, 1, 3}),
			want:     3,
		},
		{
			students: generateStudents([]int{2, 4, 1, 3}),
			want:     3,
		},
		{
			students: generateStudents([]int{1}),
			want:     1,
		},
		{
			students: generateStudents([]int{2}),
			want:     1,
		},
		{
			students: generateStudents([]int{3}),
			want:     1,
		},
		{
			students: generateStudents([]int{4}),
			want:     1,
		},
		{
			students: generateStudents([]int{1, 1}),
			want:     1,
		},
		{
			students: generateStudents([]int{2, 2}),
			want:     1,
		},
		{
			students: generateStudents([]int{3, 3}),
			want:     2,
		},
		{
			students: generateStudents([]int{4, 4}),
			want:     2,
		},
		{
			students: generateStudents([]int{1, 2}),
			want:     1,
		},
		{
			students: generateStudents([]int{3, 1, 2, 1, 1, 1, 1, 1, 1}),
			want:     3,
		},
		{
			students: generateStudents([]int{3, 1, 3, 3, 1, 3, 2, 3, 1, 3, 3, 2, 1, 2, 3, 2, 2, 1, 2, 1, 2, 1, 1, 3, 2, 1}),
			want:     13,
		},
	}

	for i, tc := range tests {
		result := MinTaxis(tc.students)
		if result != tc.want {
			t.Errorf("MinTaxis(%d) = %d, want %d", i+1, result, tc.want)
		}
	}
}

func generateStudents(groups []int) []Student {
	var students []Student
	for j, group := range groups {
		for i := 0; i < group; i++ {
			students = append(students, Student{
				GroupID: j,
				Name:    fmt.Sprintf("Student %d:%d", i, j),
			})
		}
	}
	return students
}
