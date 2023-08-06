Для того, чтобы скрипт python сработал, изначально необходимо запустить сервер frida в консоли командой:
$ frida-server -D

Саму инъекцию библиотеки gadget можно сделать двумя способами:
1. командой device.inject_library_file() в python при наличии рут-прав на устройстве, что есть в frida-script.py этого репозитория
2. с помощью пересборки приложения, дописав в один из методов главного активити, в нашем случае /.activity.MainDingtone, две строки сразу перед return этого метода:

const-string v0, "frida-gadget"
invoke-static {v0}, Ljava/lang/System;->loadLibrary(Ljava/lang/String;)V

Благодаря этому приложение будет создавать сокет, ожидая соединение от frida.
Далее с помощью
$ frida-trace -U Gadget
можно отследить URL и методы приложения.
