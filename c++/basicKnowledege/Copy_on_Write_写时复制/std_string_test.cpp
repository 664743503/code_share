#include <iostream>
#include <string>

using namespace std;

int main()
{
    string s1("hello, world");
    string s2(s1);

    cout << "sizeof(string) = " << sizeof(string) << endl;
    cout << "sizeof(s1) = " << sizeof(s1) << endl;
    
    return 0;
}

