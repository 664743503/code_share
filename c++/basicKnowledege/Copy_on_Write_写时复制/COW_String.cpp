#include <iostream>
#include <string.h>//用到字符串的操作
#include <stdio.h>//用到printf

using namespace std;

#define SIZEOF_INT sizeof(int)

class String
{
private:
    class CharProxy//用一个char的代理类实现String类的[]重载操作
    {
    public:
        CharProxy(size_t index, String & str)
            :m_index(index)
             ,m_str(str)
        {}

        char & operator=(const char & ch);

        friend ostream & operator<<(ostream & os, const CharProxy & rhs);
    private:
        size_t m_index;
        String & m_str;
    };

public:
    String();
    ~String();
    String(const char*);
    String(const String & rhs);
    String & operator=(const String & rhs);

    const char & operator[](size_t index) const{ return m_pstr[index]; }
    CharProxy operator[](size_t index);

    size_t get_ref_count()
    {
        return (*(int*)(m_pstr - SIZEOF_INT));
    }

    size_t size()
    {
        return strlen(m_pstr);
    }

    const char* c_str() const
    {
        return m_pstr;
    }

    friend ostream & operator<<(ostream & os, const String & rhs);
    friend ostream & operator<<(ostream & os, const CharProxy & rhs);

private:
    void init_ref_count()
    {
        (*(int*)(m_pstr - SIZEOF_INT)) = 1;
    }

    void increase_ref_count()
    {
        (*(int*)(m_pstr - SIZEOF_INT)) ++;
    }

    void decrease_ref_count()
    {
        (*(int*)(m_pstr - SIZEOF_INT )) --;
    }

    void release_ref_count()
    {
        decrease_ref_count();
        size_t refc = get_ref_count();
        if(refc == 0)
        {
            cout << "function:release_ref_count()" << endl;
            delete [] (m_pstr - SIZEOF_INT);
        }
    }

private:
    char* m_pstr;
};

//重载String的输出流运算符
ostream & operator<<(ostream & os, const String & rhs)
{
    os << rhs.m_pstr;
    return os;
}

//重载CharProxy的输出流运算符
ostream & operator<<(ostream & os, const String::CharProxy & rhs)
{
    os << rhs.m_str.m_pstr[rhs.m_index];
    return os;
}

String::String()
    :m_pstr(new char[SIZEOF_INT + 1]())//前SIZEOF_INT个字节用于存放引用计数，最后1个字节存放\0，下同
{
    cout << "function:String()" << endl; 
    m_pstr += SIZEOF_INT;//初始化时移动指针到第五个字节，然后开始存放字符串，下同
    init_ref_count();
}

String::String(const char* pstr)
    :m_pstr(new char(strlen(pstr) + SIZEOF_INT + 1))
{
    cout << "function:String(const char*)" << endl;
    m_pstr += SIZEOF_INT;
    init_ref_count();
    strcpy(m_pstr, pstr);
}

String::String(const String & rhs)
    :m_pstr(rhs.m_pstr)
{
    cout << "function:String(const String & rhs)" << endl;
    increase_ref_count();
}

String & String::operator=(const String & rhs)
{
    if(this != &rhs)
    {
        release_ref_count();//先处理原String的引用计数
        m_pstr = rhs.m_pstr;//然后指针赋值
        increase_ref_count();//最后，现在的String的引用计数加1
    }
    return *this;//返回自身引用
}

/* 
 * 下标访问运算符无法区分是进行读操作还是写操作
 * 所以在用的时候，都会进行深拷贝
 * 我们用CharProxy来区分读操作和写操作
 * 1.读操作用CharProxy的<<重载来实现
 * 2.写操作用String的[]重载和CharProxy的=重载来实现
 */
String::CharProxy String::operator[](size_t index)
{
    return CharProxy(index, *this);
}

char & String::CharProxy::operator=(const char & ch)
{
    if(m_str.get_ref_count() > 1)
    {
        m_str.decrease_ref_count();
        char* p_temp = new char[m_str.size() + SIZEOF_INT + 1]();//深拷贝
        strcpy(p_temp + SIZEOF_INT, m_str.m_pstr);
        m_str.m_pstr = p_temp;
        m_str.m_pstr += SIZEOF_INT;
        m_str.init_ref_count();
    }
    m_str.m_pstr[m_index] = ch;
    return m_str.m_pstr[m_index];
}

String::~String()
{
    cout << "function:~String()" << "  str = " << m_pstr << endl;
    release_ref_count();
}

void test1()
{
    String s1;
    String s2(s1);
    cout << "s1 = " << s1 << endl;
    cout << "s2 = " << s2 << endl;
    cout << "s1 ref count = " << s1.get_ref_count() << endl;
    cout << "s2 ref count = " << s2.get_ref_count() << endl;
    printf("s1 addr = %p\n", s1.c_str());
    printf("s2 addr = %p\n", s2.c_str());

}

void test2()
{
    String s3("hello 333");
    String s4(s3);
    String s5("hello 555");
    /* s3 = s5; */
    s5 = s3;
    s5[0] = 'H';
    cout << "s3 = " << s3 << endl;
    cout << "s5 = " << s5 << endl;
    cout << "s3 ref count = " << s3.get_ref_count() << endl;
    cout << "s5 ref count = " << s5.get_ref_count() << endl;
    printf("s3 addr = %p\n", s3.c_str());
    printf("s5 addr = %p\n", s5.c_str());

   	cout << endl <<"执行读操作..." << endl << "s4[0] = " << s4[0] << endl;
	cout << "s3' refcount = " << s3.get_ref_count() << endl;
	cout << "s4' refcount = " << s4.get_ref_count() << endl;
	cout << "s5' refcount = " << s5.get_ref_count() << endl;
}

int main()
{
    //test1();
    test2();
}
