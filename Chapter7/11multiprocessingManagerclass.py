from multiprocessing import Process, Manager, Event

def child(ns, event):
    ns.my_list.append(1)
    ns.my_list.append(2)
    ns.my_list.append(3)
    ns.my_list.append("new value")
    ns.my_value = 3.14
    event.set()

def parent(ns, event):
    print(f'my_list before putting event flag: {ns.my_list}')
    print(f'my_value before putting event flag: {ns.my_value}')
    event.wait()
    print(f'my_list after putting event flag: {ns.my_list}')
    print(f'my_value after putting event flag: {ns.my_value}')

if __name__ == '__main__':
    mgr = Manager()
    namespace = mgr.Namespace() # common namespace
    namespace.my_list = mgr.list() # creating a list
    # initialize a variable
    namespace.my_value = mgr.Value('d', 0.0)

    event = Event()
    child_process = Process(
        target=child,
        args=(namespace, event),
    )
    parent_process = Process(
        target=parent,
        args=(namespace, event),
    )
    parent_process.start()
    child_process.start()

    parent_process.join()
    child_process.join()