class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> triangle = new ArrayList<>();
        if (numRows <= 0) return triangle;

        for (int r = 0; r < numRows; r++) {
            List<Integer> row = new ArrayList<>();
            row.add(1); 
            for (int c = 1; c < r; c++) {
                int aboveLeft  = triangle.get(r - 1).get(c - 1);
                int aboveRight = triangle.get(r - 1).get(c);
                row.add(aboveLeft + aboveRight);
            }

            if (r > 0) row.add(1);
            triangle.add(row);
        }
        return triangle;
    }
}
