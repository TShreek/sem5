#include <iostream>
#include <limits>
#include <stdexcept>
#include <type_traits>

class SafeConversion {
public:
    // Safe cast with range checks
    template <typename Target, typename Source>
    static Target cast(Source value) {
        if (value > static_cast<Source>(std::numeric_limits<Target>::max())) {
            throw std::overflow_error("Overflow detected during cast");
        }
        if (value < static_cast<Source>(std::numeric_limits<Target>::min())) {
            throw std::underflow_error("Underflow detected during cast");
        }
        return static_cast<Target>(value);
    }

    // Safe comparison
    template <typename T, typename U>
    static bool compare(T a, U b) {
        if constexpr (std::is_signed<T>::value && std::is_unsigned<U>::value) {
            return a >= 0 && static_cast<std::make_unsigned_t<T>>(a) <= b;
        } else if constexpr (std::is_unsigned<T>::value && std::is_signed<U>::value) {
            return b >= 0 && a <= static_cast<std::make_unsigned_t<U>>(b);
        } else {
            return a <= b;
        }
    }

    // Safe truncation
    template <typename Target, typename Source>
    static Target truncate(Source value) {
        return cast<Target>(value);
    }

    // Safe float to integer conversion
    template <typename Target>
    static Target float_to_int(double value) {
        if (value > static_cast<double>(std::numeric_limits<Target>::max()) ||
            value < static_cast<double>(std::numeric_limits<Target>::min())) {
            throw std::overflow_error("Floating-point value out of range");
        }
        return static_cast<Target>(value);
    }
};

int main() {
    try {
        // Test Case 1: Safe cast within range
        int smallValue = SafeConversion::cast<int>(100LL);
        std::cout << "Test 1 Passed: " << smallValue << "\n";

        // Test Case 2: Safe cast overflow
        try {
            SafeConversion::cast<int>(123456789012345LL);
        } catch (const std::exception& e) {
            std::cout << "Test 2 Passed: " << e.what() << "\n";
        }

        // Test Case 3: Safe cast underflow
        try {
            SafeConversion::cast<int>(-123456789012345LL);
        } catch (const std::exception& e) {
            std::cout << "Test 3 Passed: " << e.what() << "\n";
        }

        // Test Case 4: Safe unsigned to signed comparison
        if (SafeConversion::compare(-1, 10U)) {
            std::cout << "Test 4 Failed\n";
        } else {
            std::cout << "Test 4 Passed\n";
        }

        // Test Case 5: Safe signed to unsigned comparison
        if (SafeConversion::compare(10, -1U)) {
            std::cout << "Test 5 Failed\n";
        } else {
            std::cout << "Test 5 Passed\n";
        }

        // Test Case 6: Safe truncation within range
        short truncatedValue = SafeConversion::truncate<short>(100);
        std::cout << "Test 6 Passed: " << truncatedValue << "\n";

        // Test Case 7: Safe truncation overflow
        try {
            SafeConversion::truncate<short>(70000);
        } catch (const std::exception& e) {
            std::cout << "Test 7 Passed: " << e.what() << "\n";
        }

        // Test Case 8: Safe float to int conversion
        int floatToInt = SafeConversion::float_to_int<int>(99.99);
        std::cout << "Test 8 Passed: " << floatToInt << "\n";

        // Test Case 9: Safe float to int overflow
        try {
            SafeConversion::float_to_int<int>(1e20);
        } catch (const std::exception& e) {
            std::cout << "Test 9 Passed: " << e.what() << "\n";
        }

        // Test Case 10: Safe float to int underflow
        try {
            SafeConversion::float_to_int<int>(-1e20);
        } catch (const std::exception& e) {
            std::cout << "Test 10 Passed: " << e.what() << "\n";
        }

    } catch (const std::exception& e) {
        std::cerr << "Unexpected error: " << e.what() << "\n";
    }

    return 0;
}

