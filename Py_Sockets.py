import socket
import threading
import select

# region #* Сокеты, сервер ----------------------------------------------------
"""Сокеты — кросс-платформенный механизм для обмена данными между отдельными
процессами. Эти процессы могут работать на разных серверах, они могут быть
написаны на разных языках, и, прежде всего, программа на Python осуществляет
системные вызовы и взаимодействие с ядром операционной системы.
Как правило, для организации сетевого взаимодействия нужен сервер, который
изначально создает некое соединение и начинает «слушать» все запросы, которые
поступают в него и программа-клиент, которая присоединяется к серверу и
отправляет ему нужные данные.
Прежде всего импортируется модуль soket."""
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""создание объект типа socket из модуля socket. В него передаются параметры. В
данном случае это некоторое семейство — address family, конкретная константа
AF_INET, а также тип сокета - .SOCK_STREAM - потоковый сокет. """
sock.bind(('127.0.0.1', 10001))  # max port - 65535
"""Системный вызов bind регистрирует адресную пару в операционной системе.
В метод bind передается адресная пара, это host, в данном случае мы передаем
127.0.0.1, и порт.
127.0.0.1 означает, что сервер будет слушать все входящие соединения только
локально на одной машине. Если указать пустую строчку, либо адрес 0.0.0.0, то
сервер будет слушать входящие соединения со всех интерфейсов.
Порт — это целочисленная константа. Существуют зарезервированные порты,
например, 80-й порт, 43-й порт, 443-й порт. Как правило, порты с номерами до
2000 являются системными, и необходимо использовать адреса больше значений
2000. Максимальное значение для порта — это 65535."""
sock.listen(socket.SOMAXCONN)
"""Для того чтобы начать принимать соединения, вызвается метод listen.
У метода listen есть необязательный параметр — это так называемый backlog, или
размер очереди входящих соединений, которые еще не обработаны, для которых не
был вызван метод accept.
Если сервер будет не успевать принимать входящие соединения, то все эти
соединения будут копиться в этой очереди, и если она превысит это максимальное
значение, то операционная система выдаст ошибку ConnectionRefused для
клиентской программы."""
conn, addr = sock.accept()
"""Далее вызывается метод accept, который принимает входящее клиентское
соединение. accept по умолчанию заблокируется, до тех пор, пока не появится
клиентское соединение. Если клиент вызовет метод connect, то метод accept
вернет объект, который будет являться полнодуплексным каналом. У этого объекта
будут доступны методы записи в этот канал и методы чтения."""
while True:
    """в бесконечном цикле"""
    data = conn.recv(1024)  # вызывается чтение из полнодуплексного канала
    if not data:
        """Если ничего не прочитано, это означает, что клиент закрыл соединение
        и необходимо тоже прекратить работу"""
        break
    # process data
    print(data.decode('utf-8'))

conn.close()  # закрытие объекта дуплексного канала
sock.close()  # закрытие объекта сокета
# ------------------------------------------------------

"""Все сетевые программы должны уметь обрабатывать ошибки. В т.ч. для обработки
ошибок используются контекстные менеджер.
Ниже точно такой же серверный код написанный через контекстный менеджер"""

with socket.socket() as sock:
    sock.bind(('127.0.0.1', 10001))
    sock.listen()

    while True:
        conn, addr = sock.accept()
        with conn:
            while True:
                data = conn.resv(1024)  # вызов метода resv для сокета
                if not data:
                    break
                print(data.decode('utf-8'))

# endregion -------------------------------------------------------------------

# region #* Сокеты, клиент ----------------------------------------------------

sock = socket.socket()
# Для того чтобы установить соединение с сервером, необходимо создать объект
# типа socket.socket.
# По умолчанию создается потоковый сокет с семейством address family AF_INET.
sock.connect(('127.0.0.1', 10001))
# После этого вызвается метод connect. Connect заблокируется до тех пор, пока
# сервер со своей стороны не вызовет метод accept.
sock.sendall(b"ping".encode('utf-8'))  # передаются байты а не строки
# После того как системный вызов connect отработал, сокет готов к работе, и для
# него можно вызывать методы send, sendall или recv, для того чтобы получать
# данные с сервера.
sock.close()
""" То есть, по сути, получился такой же полнодуплексный канал, с которым
можно работать, отправлять и получать данные. После того как завершена
работа с клиентским сокетом, необходимо вызвать метод close. """

# Или более короткая запись:
sock = socket.create_connection(('127.0.0.1', 10001))
sock.sendall(b"ping".encode('utf-8'))  # при работе по сети передаются байты
sock.close()

"""Сетевые протоклы должны содержать в себе обработчики ошибок. В том числе для
этого, используют также контекстные менеджеры.
Ниже тот же код написанный с пмощью контекстного менеджера:"""
with socket.create_connection(('127.0.0.1', 10001)) as sock:
    sock.sendall(b"ping".encode('utf-8'))
# endregion -------------------------------------------------------------------

# region #* Таймаут, обработка ошибок -----------------------------------------
"""По умолчанию все вызовы для объекта соединения, например вызов recv, или
вызов send, будут заблокированы до тех пор, пока данные на другой стороне
не будут обработаны и не будет получен ответ. Это может завесить систему.
По умолчанию таймаута нет, то есть клиент/сервер может ждать ответ вечно."""

# ? для серверной части
with socket.socket() as sock:
    sock.bind(('127.0.0.1', 10001))
    sock.listen()

    while True:
        conn, addr = sock.accept()
        conn.settimeout(5)  # устновка timeoute,если None - значит по умолчанию
        """После получения соединения (accept), вызываем метод settimeout для
        объекта. И устанавливаем таймаут (5). По умолчанию таймаут None.
        Если (0) - сокет переходит в неблокирующий режим"""
        with conn:
            while True:
                try:
                    data = conn.resv(1024)
                except socket.timeout:  # обработка ошибок по таймауту
                    print("close connection by timeout")
                    break

                if not data:
                    break
                print(data.decode('utf-8'))
# --------------------------------------------
# ? для клиентской части
with socket.create_connection(('127.0.0.1', 10001), 5) as sock:
    """устновка connect таймаут (5) прямо в конструкции создания соединения.
    Распространяется только на установку соединения с сервером"""
    sock.settimeout(2)
    """установка socket read таймаута, на все текущие операции с сокетом"""
    try:
        sock.sendall(b"ping".encode('utf-8'))
    except socket.timeout:
        """Исключение обрабатывается если не смогли сделать обработку команды
        сокета (set, get, итп)"""
        print("send data timeoute")
    except socket.error as ex:  # базовый класс обработки исключений сокета
        """Исключени возникает при любой другой сетевой ощибке"""
        print("send data error", ex)
# endregion -------------------------------------------------------------------

# region #* Обработка нескольких соединений -----------------------------------
"""Если соединение принято и начата его обработка, в том же самом потоке сервер
не может принимать новые соединения. Если будет большое количество клиентов, то
все остальные клиенты будут вынуждены ждать, пока будет закончена работа с
первым соединением. """
# ? для серверной части
with socket.socket() as sock:
    sock.bind(('127.0.0.1', 10001))
    sock.listen()

    while True:
        conn, addr = sock.accept()
        """ #? в этом месте можно разделить соединения на потоки или процессы
        создание многопроцессорности оправдано только когда соединений мало, а
        задачи по обработке - глобальные. В остальных методах - потоки. Но,
        потоки работают на 1 ядре и упираются в GIL"""
        with conn:
            while True:
                data = conn.resv(1024)  # вызов метода resv для сокета
                if not data:
                    break
                print(data.decode('utf-8'))
# ---------------------------------------------------------


# ? Для разделения на потоки используются функции или классы:
def process_request(conn, addr):
    """функция обработки поступающих запросов"""
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode('utf-8'))


with socket.socket() as sock:
    """Потоки запускаются в контексте, чтобы не заботиться о закрытии"""
    sock.bind('', 10001)
    sock.listen()
    while True:
        conn, addr = sock.accept()
        """исполняемый код, содержащщий разделения соединения на потоки
        (threading) и передачи в них функции с исполняемым кодом
        (process_request)."""
        th = threading.Thread(target=process_request, args=(conn, addr))
        th.start()
# ---------------------------------------------------------

# ? Можно использовать разделение на потоки и процессы одновременно:
with socket.socket() as sock:
    sock.bind('', 10001)
    sock.listen()
    # в этом месте вызывается fork() для линукс, и создаются дубли процессов
    while True:
        conn, addr = sock.accept()  # вызывается свой для каждого процесса
        with conn:
            # в этом блоке кода создаются потоки threading()
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(data.decode('utf-8'))
# endregion -------------------------------------------------------------------

# region #* Исполнение кода в 1 поток. Модуль Select() ------------------------
"""В операционной системе существует модуль select, позволяеющий организовать
работу с неблокирующим вводом-выводом.
"""
sock = socket.socket()  # создание объекта сокета
sock.bind()
sock.listen()

conn1, addr = sock.accept()
conn2, addr = sock.accept()

conn1.setblocking(0)  # перевод соединения в неблокирующий режим. В этом режиме
conn2.setblocking(0)  # вместо исключения идет некий ответ об ошибке

# ? образцец для Линукс
epoll = select.epoll()  # создание объекта epoll
epoll.register(conn1.fileno(), select.EPOLLIN | select.EPOLLOUT)
"""в обхекте epoll регистриуются файловые дескрипторы coll1.fileno, а также
маску, то есть говорим на какие события файловых дескрипторов мы подписываемся.
Чтение и запись в совектах """
epoll.register(conn2.fileno(), select.EPOLLIN | select.EPOLLOUT)
conn_map = {conn1.fileno(): conn1, conn2.fileno(): conn2, }
# создается словрь объектов файловых соединений.

# endregion -------------------------------------------------------------------