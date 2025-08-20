#include "difference_of_squares.h"

namespace difference_of_squares {
    int sum_of_squares(int number) {
        int sum = 0;
        for (int i = 1; i <= number; i++) {
            sum += i * i;
        }
        return sum;
    }

    int square_of_sum(int number) {
        int sum = 0;
        for (int i = 1; i <= number; i++) {
            sum += i;
        }
        return sum * sum;
    }
    int difference(int number) {
        return square_of_sum(number) - sum_of_squares(number);
    }
}  // namespace difference_of_squares
