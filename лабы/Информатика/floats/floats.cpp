#include <iostream>
#include <cmath>

int main(){

    unsigned int n;
    std::cin >> n;

    unsigned int mask = 1 << 31;
    for (int i = 0; i <32; i++){
        std::cout << (bool)(n&mask);
        mask = mask >> 1;
    }
    return 0;
}
