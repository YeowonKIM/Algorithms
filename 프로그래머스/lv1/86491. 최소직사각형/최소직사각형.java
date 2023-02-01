class Solution {
    public int solution(int[][] sizes) {
        int longMax=0, shortMax=0;

//        List<Integer> shortLine = new ArrayList<>();
//        List<Integer> longLine = new ArrayList<>();

        for (int i = 0; i < sizes.length; i++) {
            if (sizes[i][0] > sizes[i][1]) {
//                shortLine.add(sizes[i][1]);
//                longLine.add(sizes[i][0]);
                if (shortMax < sizes[i][1]) {shortMax = sizes[i][1];}
                if (longMax < sizes[i][0]) {longMax = sizes[i][0];}
            } else {
//                shortLine.add(sizes[i][0]);
//                longLine.add(sizes[i][1]);
                if(shortMax < sizes[i][0]) {shortMax = sizes[i][0];}
                if (longMax < sizes[i][1]) {longMax = sizes[i][1];}
            }
        }
        return shortMax*longMax;
    }
}