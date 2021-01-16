package main

import "fmt"

func quickSort(array []int) []int {
	var right []int
	var left []int

	// 分割できなくなった時([1]みたいな)はそのまま返す
	if len(array) <= 1 {
		return array
	}

	// 基準値を設定、今回はとりあえず先頭
	baseValue := array[0]

	// 基準値と同じになった値の数も数える
	baseValueCount := 0

	// forで一つずつ取り出す。
	for _, value := range array {
		// 基準値と比較して大きかったらrightに、小さかったらleftに、一緒だったらbaseValueCountを増やす。
		if value < baseValue {
			left = append(left, value)
		} else if value > baseValue {
			right = append(right, value)
		} else {
			baseValueCount++
		}

		// 再帰的に呼び出していく分割できなくなるまで呼び出す
		left = quickSort(left)
		right = quickSort(right)
	}

	// バラバラになってる配列をくっつける。
	//基準値の配列を作る
	var baseValueArray []int
	for i := 0; i < baseValueCount; i++ {
		baseValueArray = append(baseValueArray, baseValue)
	}
	//展開して繋げる
	returnArray := append(left, baseValueArray...)
	returnArray = append(returnArray, right...)
	return returnArray
}

func main() {
	inputArray := []int{2, 1, 3, 4, 2, 6, 1, 7, 1, 4, 5}
	fmt.Println(inputArray)
	outputArray := quickSort(inputArray)
	fmt.Println(outputArray)
}
