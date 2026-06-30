 candidates.sort()
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):

                # skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])

                # use i + 1 because each number can be used only once
                backtrack(i + 1, path, total + candidates[i])

                path.pop()

        backtrack(0, [], 0)
        return res
