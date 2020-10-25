# 学习笔记

## 数组、链表、跳表

### （一）数组

内存中开辟连续地址，可在O(1)时间内查询任何下标的元素。但是由于地址连续，插入和删除元素的时间复杂度较高。

例如：
1. 数组末尾插入元素和删除元素，时间复杂度都是O(1)。

2. 数组的其余位置插入元素，首先将从指定位置到末尾的所有元素后移一位，然后在指定位置插入元素，时间复杂度是O(n)，n是数组长度。

3. 数组的其余位置删除元素，则在删除元素后，将从指定位置后一位到末尾的所有元素前移一位，时间复杂度是O(n)，其中n是数组长度。

### （二）链表

内存地址不连续，每个元素是一个节点，每个节点都有相应的值。链表有两种类型。

1. 单向链表：节点包含指向下一个节点的指针。

2. 双向链表：节点包含指向上一个节点的指针和指向下一个节点的指针。

链表中，通常需要指定头节点和尾节点。

3. 在链表中插入和删除元素时，无论插入和删除的元素是在链表的头部、尾部还是中间，只需要改变相邻节点的指针指向的节点，时间复杂度都是O(1)。

4. 由于链表的内存地址不连续，所以不能根据下标直接查询元素，需要遍历节点才能查询元素，查询元素的时间复杂度是O(n)，其中n是链表中的元素数量。

### （三）跳表

1. 实现基于链表，其目的是降低链表的查询元素的时间复杂度。只适用于元素有序的情况。

2. 跳表对标平衡二叉搜索树和二分查找，插入、删除、查询元素的时间复杂度都是O(log n)，其中n是元素数量。

3. 跳表通过升维的方式进行加速，从一维到二维，包含更多信息。具体实现为在原始链表的基础上增加多级索引，每级索引包含的节点数量依次减少。

4. 跳表的空间复杂度和数组、链表一样是O(n)，但是由于跳表有多级索引，实际使用空间超过数组和链表。

### 总结

1. 数组的查询元素的时间复杂度是O(1)，插入和删除元素的时间复杂度是O(n)。所以当需要经常查询元素时，使用数组更合适。

2. 链表的查询元素的时间复杂度是O(n)，插入和删除元素的时间复杂度是O(1)。所以当需要经常插入和删除元素时，使用链表更合适。

## 栈、队列、双端队列、优先队列

### （一）栈、队列

Stack：First In Last Out，添加、删除元素的时间复杂度是O(1)。

Queue：First In First Out，添加、删除元素的时间复杂度是O(1)。

由于元素无序，查询的时间复杂度都是O(n)，其中n是元素数量。

### （二）双端队列

Deque：结合了栈和队列的特点，可在头和尾两端添加和删除元素。

双端队列的各项操作的时间复杂度和栈与队列相同，添加、删除元素的时间复杂度是O(1)，查询的时间复杂度是O(n)，其中n是元素数量。

### （三）优先队列

Priority Queue：元素具有优先级顺序，每次取出优先级最高的元素（例如最大值或最小值）。

添加元素的时间复杂度是O(1)，取出元素的时间复杂度是O(log n)，其中n是元素数量。

### （四）工程实现（Java)

1. Stack是具体类，可直接用于实例化对象，但是建议用Deque代替Stack。

2. Queue和Deque是接口，需要通过实现类实例化对象，LinkedList是常用的实现类。

3. PriorityQueue是Queue的实现类。

## 课后作业

#### 1.用 addfirst 或 addlast 这套新的 API 改写 Deque 的代码


```
/*
源码：
*/
Deque<String> deque = new LinkedList<String>();

deque.push("a");
deque.push("b");
deque.push("c");
System.out.println(deque);

String str = deque.peek();
System.out.println(str);
System.out.println(deque);
while (deque.size() > 0) {
    System.out.println(deque.pop());
}
System.out.println(deque);
```

```
/*
改写：
*/
Deque<String> deque = new LinkedList<String>();

deque.addFirst("a");
deque.addFirst("b");
deque.addFirst("c");
System.out.println(deque);

String str = deque.peekFirst();
System.out.println(str);
System.out.println(deque);
while (deque.size() > 0) {
    System.out.println(deque.removeFirst());
}
System.out.println(deque);
```

#### 2. 分析Queue和Priority Queue源码

##### Queue

Queue是一个接口，继承了Collection接口。Queue接口只包含抽象方法。

Queue接口包含以下抽象方法。
添加元素接口
1. boolean add(E e)：往队列尾部添加元素，如果添加成功则返回true，如果因为容量限制导致添加失败则抛出IllegalStateException异常。

2. boolean offer(E e)：往队列尾部添加元素，如果添加成功则返回true，如果因为容量限制导致添加失败则返回false。和add区别在与不会因为队列已满抛异常。

删除元素接口
3. E remove()：删除队列头部的元素并返回，如果队列为空则抛出NoSuchElementException。

4. E poll()：删除队列头部的元素并返回，如果队列为空则返回null（与remove不同）。

获取队列元素接口
5. E element()：返回队列头部的元素（不从队列删除元素），如果队列为空则抛出NoSuchElementException。

6. E peek()：返回队列头部的元素（不从队列删除元素），如果队列为空则返回null。

##### PriorityQueue

PriorityQueue是基于二叉堆形式实现的无界队列。队列中元素类型必须是可比较的，构造函数如果没有传入Comparator默认是自然排序。
PriorityQueue继承了AbstractQueue，AbstractQueue实现Queue接口，即PriorityQueue拥有Queue的方法和特征。

1. boolean add(E e)
```
public boolean add(E e) {
    if (offer(e))
        return true;
    else
        throw new IllegalStateException("Queue full");
}
```

2. E remove()
```
public E remove() {
    E x = poll();
    if (x != null)
        return x;
    else
        throw new NoSuchElementException();
}

```

3. E element()
```
public E element() {
    E x = peek();
    if (x != null)
        return x;
    else
        throw new NoSuchElementException();
}

```

4. PriorityQueue实现了扩容，查找元素对应下标的方法，通过数组管理元素，元素需要是可以比较的对象，如果不能比较需要明确指定比较器。
5. void grow(int minCapacity)：扩容方法

   --当前长度小于64的时候，每次扩容增加2，大于等于64后，每次扩容增加当前长度的一半
   --按照通用扩容方法扩容后，如果超范围，就按照指定大小进行扩容
   --指定的大小超范围，就直接扩容到最大范围
   
6. int indexOf(Object o)：查找元素对应下标

   --通过循环遍历当前数组，逐个进行比较，有相等的，直接返回对应元素下标，没有相等的返回-1
