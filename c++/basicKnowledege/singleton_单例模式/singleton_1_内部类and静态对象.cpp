#include <iostream>
using namespace std;

// 单例模式1：内部类+静态对象实现

// 单例类
class Singleton
{
private:
    class AutoRelease
    {
    public:
        AutoRelease(){ cout << "AutoRelease()" << endl; }
        ~AutoRelease()
        {
            if(m_pInstance != nullptr)
            {
                cout << "~AutoRelease()" << endl;
                delete m_pInstance;
            }
        }
    };

public:
    // 获取对象
    // 在多线程下是非线程安全的，如果想要线程安全，则需要加锁
    static Singleton* getInstance()
    {
        if(nullptr == m_pInstance)
        {
            m_pInstance = new Singleton();
        }
        return m_pInstance;
    }

private:
    Singleton() {cout << "Singleton()" << endl;}
    ~Singleton() {cout << "~Singleton()" << endl;}
    static Singleton* m_pInstance;
    static AutoRelease m_auto;
};

// 当用到单例模式时，对象才初始化，称之为饿汉模式(懒汉模式，懒加载)，优点：节省空间，缺点：需要加锁，浪费效率
Singleton* Singleton::m_pInstance = nullptr;

// 在进入main函数之前就创建在堆空间里面，所以是线程安全的，又称饱汉模式。优点：节省效率，缺点：浪费堆空间。
/* Singleton* Singleton::m_pInstance = getInstance(); */
Singleton::AutoRelease Singleton::m_auto;

int main()
{
    Singleton* p1 = Singleton::getInstance();
    Singleton* p2 = Singleton::getInstance();
    cout << "p1 = " << p1 << endl;
    cout << "p2 = " << p2 << endl;
    return 0;
}
