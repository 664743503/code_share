#include <iostream>

using namespace std;

#define CODE_OPEN 1

class INT
{
    friend ostream& operator<<(ostream& os, const INT& i);

public:
    INT(int i)
        :m_i(i)
    {}

    INT& operator++()
    {
        ++(this->m_i);
        return *this;
    }

#if CODE_OPEN
    const INT operator++(int)
    {
        INT temp = *this;
        ++(*this);//调用上面的重载的++函数，即++了this->m_i
        return temp;
    }
#endif

    INT& operator--()
    {
        --(this->m_i);
        return *this;
    }

#if CODE_OPEN
    const INT operator--(int)//前面加const表示返回值是const的
    {
        INT temp = *this;
        --(*this);
        return temp;
    }
#endif

    int& operator*() const//后面加const表示该函数不修改成员变量
    {
        return (int&)m_i;
    }
private:
    int m_i;
};

ostream& operator<<(ostream& os, const INT& i)
{
    os << "[" << i.m_i << "]";
    return os;
}

int main()
{
    INT I(5);
    
    /*
     * I++调用流程
     * 1.首先进入const INT operator++(int)
     * 2.在++(*this)这里，跳转到重载的INT& operator++()函数
     * 3.const INT operator++(int)执行完之后，执行重载的<<操作
     * cout打印的是temp的值，实际上I是++了的。
     * 表现形式：先输出，然后++
     */
    cout << I++ << endl;//[5]

    //直接调用INT& operator++()函数
    //表现形式：先++，再输出
    cout << ++I << endl;//[7]

    //与I++类似
    //先输出，然后--
    cout << I-- << endl;//[7]

    //先--，然后输出
    cout << --I << endl;//[5]

    cout << *I << endl;//5

    return 0;
}
