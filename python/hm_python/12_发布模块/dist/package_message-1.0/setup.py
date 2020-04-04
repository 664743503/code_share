from distutils.core import setup

setup(name="package_message",
      version="1.0",
      description="发送和接受消息模块",
      author="SY",
      author_email="664743503@qq.com",
      url="None",
      py_modules=["package_message.send_message",
                "package_message.receive_message"],
     )

