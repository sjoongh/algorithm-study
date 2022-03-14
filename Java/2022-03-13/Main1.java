package 2022-03-13;

// S : abcde
// interval : [ [1,3], [1,4], [2,5] ]
// interval에 따라서 S 문자열의 문자 위치 변경
class Solution {
    // 해당 인덱스만 변경되게 하려면 toCharArray()로 쪼갠다음에
	// 처음과 끝만 변경해주고 new String(arr)로 보내주면 될 듯.
	private static String changeString(String str) { // 범위 전체를 바꾸는 함수
		// 기준문자열.toCharArray() --> 문자열을 char형으로 쪼갬 --> char 배열에 넣어줘야함
		char[] arr = str.toCharArray();
		System.out.println(arr);
		for (int i = 0; i < str.length() / 2; i++) { // 문자열 switch는 문자열 길이의 반만 하면됨
			char ch = arr[i];
			arr[i] = arr[arr.length -1 -i];
			arr[arr.length -1 -i] = ch;
		}
		System.out.println(arr);
		
		return new String(arr); // char --> String 인스턴스 생성
	}
	
	public static void solution(String S, int[][] interval) {
		for (int i = 0; i < interval.length; i++) { // 0,1,2 돌아감
			int startIdx = interval[i][0] -1; // 숫자는 1이지만 배열은 0부터 시작하므로 -1
			int endIdx = interval[i][1]; // subString이 가져간 범위 이후의 문자열 --> changeString에 있는 for문이 < 까지만 돌아가도록 하는 역할
			// 변경해야 하는 문자열 범위만 잘라냄 --> subString으로 --> 해당 영역만 함수로 보냄
			String subString = changeString(S.substring(startIdx, endIdx));
			String start = S.substring(0, startIdx); // 1번이 바뀌면 ""이 나옴
			String end = S.substring(endIdx); // 문자열의 마지막이 바뀔때는 ""로 처리
			S = start + subString + end;
			System.out.println(S+" test4");
	}
	
}
}
