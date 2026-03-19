class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;
        int initDay = startday;
        for (int i = 0; i < schedules.length; i++) {
            boolean flag = false;
            int pos = schedules[i] + 10;
            
            if (pos % 100 >= 60) {
                pos += 100; // 시간 정리
                pos -= 60; // 분 정리
            }
            
            for (int j = 0; j < timelogs[i].length; j++) {
                if (startday == 6) { // 토요일
                    startday++;
                    continue;
                }
                if (startday == 7) { // 일요일
                    startday = 1;
                    continue;
                }
                
                if (pos < timelogs[i][j]) {
                    flag = true;
                    break;
                } 
                startday++;
            }
            
            if (!flag) answer++;
            startday = initDay;
        }
        
        return answer;
    }
}

// 스케쥴 시간 + 10분 
// 2중 for
// 6 or 7 이면 무시 
// 7이면 다시 day = 1 초기화
// flag 활용 cnt++ 체크
//  flag는 값 초과시 flag > true

// 시간 체크 필요 60분 넘어가면 시를 올려야함
// 시간 % 100 60이 넘는가?
//   넘으면 > 시간 + 100 & 시간 - 60
