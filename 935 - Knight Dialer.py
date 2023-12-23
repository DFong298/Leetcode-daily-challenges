class Solution:
    # Lobotomize solution lol
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        zero = one = two = three = four = five = six = seven = eight = nine = 1
        for i in range(n-1):
            zero, one, two, three, four, five, six, seven, eight, nine = (
                (four + six) % MOD,
                (eight + six) % MOD,
                (seven + nine) % MOD,
                (eight + four) % MOD,
                (nine + three + zero) % MOD,
                0,
                (zero + seven + one) % MOD,
                (six + two) % MOD,
                (one + three) % MOD,
                (four + two) % MOD
            )

        return (zero + one + two + three + four + five + six + seven + eight + nine) % MOD