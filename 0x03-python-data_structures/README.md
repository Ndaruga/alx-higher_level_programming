# 0x03. Python - Data Structures: Lists, Tuples

   <h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://docs.python.org/3/tutorial/introduction.html#lists" title="3.1.3. Lists" target="_blank">3.1.3. Lists</a> </li>
<li><a href="https://docs.python.org/3/tutorial/datastructures.html" title="Data structures" target="_blank">Data structures</a> (<em>until <code>5.3. Tuples and Sequences</code> included</em>)</li>
<li><a href="https://www.youtube.com/watch?v=A1HUzrvS-Pw" title="Learn to Program 6 : Lists" target="_blank">Learn to Program 6 : Lists</a> </li>
</ul>

<h2 class="gap">Tasks</h2>

<h3>0. Print a list of integers</h3>
<p>Write a function that prints all integers of a list.</p>

<ul>
<li>Prototype: <code>def print_list_integer(my_list=[]):</code></li>
<li>Format: one integer per line. See example</li>
<li>You are not allowed to import any module</li>
<li>You can assume that the list only contains integers</li>
<li>You are not allowed to cast integers into strings</li>
<li>You have to use <code>str.format()</code> to print integers</li>
</ul>

<pre><code>frank@ubuntu:~/0x03$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__(&#39;0-print_list_integer&#39;).print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

frank@ubuntu:~/0x03$ ./0-main.py
1
2
3
4
5
frank@ubuntu:~/0x03$ 
</code></pre>

<h3>1. Secure access to an element in a list</h3>
<p>Write a function that retrieves an element from a list like in C.</p>

<ul>
<li>Prototype: <code>def element_at(my_list, idx):</code></li>
<li>If <code>idx</code> is negative, the function should return <code>None</code></li>
<li>If <code>idx</code> is out of range (&gt; of number of element in <code>my_list</code>), the function should return <code>None</code> </li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>try/except</code></li>
</ul>

<pre><code>frank@ubuntu:~/0x03$ cat 1-main.py
#!/usr/bin/python3
element_at = __import__(&#39;1-element_at&#39;).element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print(&quot;Element at index {:d} is {}&quot;.format(idx, element_at(my_list, idx)))

frank@ubuntu:~/0x03$ ./1-main.py
Element at index 3 is 4
frank@ubuntu:~/0x03$ 
</code></pre>

<h3>2. Replace element</h3>
<p>Write a function that replaces an element of a list at a specific position (like in C).</p>

<ul>
<li>Prototype: <code>def replace_in_list(my_list, idx, element):</code></li>
<li>If <code>idx</code> is negative, the function should not modify anything, and returns the original list</li>
<li>If <code>idx</code> is out of range (&gt; of number of element in <code>my_list</code>), the function should not modify anything, and returns the original list</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>try/except</code></li>
</ul>

<pre><code>frank@ubuntu:~/0x03$ cat 2-main.py
#!/usr/bin/python3
replace_in_list = __import__(&#39;2-replace_in_list&#39;).replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

frank@ubuntu:~/0x03$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
frank@ubuntu:~/0x03$ 
</code></pre>

<h3>3. Print a list of integers... in reverse!</h3>
<p>Write a function that prints all integers of a list, in reverse order.</p>

<ul>
<li>Prototype: <code>def print_reversed_list_integer(my_list=[]):</code></li>
<li>Format: one integer per line. See example</li>
<li>You are not allowed to import any module</li>
<li>You can assume that the list only contains integers</li>
<li>You are not allowed to cast integers into strings</li>
<li>You have to use <code>str.format()</code> to print integers</li>
</ul>

<pre><code>frank@ubuntu:~/0x03$ cat 3-main.py
#!/usr/bin/python3
print_reversed_list_integer = __import__(&#39;3-print_reversed_list_integer&#39;).print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

frank@ubuntu:~/0x03$ ./3-main.py
5
4
3
2
1
frank@ubuntu:~/0x03$ 
</code></pre>

<h3>4. Replace in a copy</h3>
<p>Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).</p>

<ul>
<li>Prototype: <code>def new_in_list(my_list, idx, element):</code></li>
<li>If <code>idx</code> is negative, the function should return a copy of the original <code>list</code></li>
<li>If <code>idx</code> is out of range (&gt; of number of element in <code>my_list</code>), the function should return a copy of the original <code>list</code></li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>try/except</code></li>
</ul>

<pre><code>frank@ubuntu:~/0x03$ cat 4-main.py
#!/usr/bin/python3
new_in_list = __import__(&#39;4-new_in_list&#39;).new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

frank@ubuntu:~/0x03$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
frank@ubuntu:~/0x03$ 
</code></pre>


<h3>5. Can you C me now?</h3>
<p>Write a function that removes all characters <code>c</code> and <code>C</code> from a string.</p>

<ul>
<li>Prototype: <code>def no_c(my_string):</code></li>
<li>The function should return the new string</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use <code>str.replace()</code></li>
</ul>

<pre><code>frank@ubuntu:~/0x03$ cat 5-main.py
#!/usr/bin/env python3
no_c = __import__(&#39;5-no_c&#39;).no_c

print(no_c(&quot;Best School&quot;))
print(no_c(&quot;Chicago&quot;))
print(no_c(&quot;C is fun!&quot;))

frank@ubuntu:~/0x03$ ./5-main.py
Best Shool
hiago
 is fun!
frank@ubuntu:~/0x03$ 
</code></pre>

<h3>6. Lists of lists = Matrix</h3>
<p>Write a function that prints a matrix of integers.</p>

<ul>
<li>Prototype: <code>def print_matrix_integer(matrix=[[]]):</code></li>
<li>Format: see example</li>
<li>You are not allowed to import any module</li>
<li>You can assume that the list only contains integers</li>
<li>You are not allowed to cast integers into strings</li>
<li>You have to use <code>str.format()</code> to print integers</li>
</ul>

<pre><code>frank@ubuntu:~/0x03$ cat 6-main.py
#!/usr/bin/python3
print_matrix_integer = __import__(&#39;6-print_matrix_integer&#39;).print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print(&quot;--&quot;)
print_matrix_integer()

frank@ubuntu:~/0x03$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
frank@ubuntu:~/0x03$ 
</code></pre>

<h3>7. Tuples addition</h3>
<p>Write a function that adds 2 tuples.</p>

<ul>
<li>Prototype: <code>def add_tuple(tuple_a=(), tuple_b=()):</code></li>
<li>Returns a tuple with 2 integers:

<ul>
<li>The first element should be the addition of the first element of each argument</li>
<li>The second element should be the addition of the second element of each argument</li>
</ul></li>
<li>You are not allowed to import any module</li>
<li>You can assume that the two tuples will only contain integers</li>
<li>If a tuple is smaller than 2, use the value <code>0</code> for each missing integer</li>
<li>If a tuple is bigger than 2, use only the first 2 integers</li>
</ul>

<pre><code>frank@ubuntu:~/0x03$ cat 7-main.py
#!/usr/bin/python3
add_tuple = __import__(&#39;7-add_tuple&#39;).add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

frank@ubuntu:~/0x03$ ./7-main.py
(89, 100)
(2, 89)
(1, 89)
frank@ubuntu:~/0x03$ 
</code></pre>

<h3>8. More returns!</h3>
<p>Write a function that returns a tuple with the length of a string and its first character.</p>

<ul>
<li>Prototype: <code>def multiple_returns(sentence):</code></li>
<li>If the sentence is empty, the first character should be equal to <code>None</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>frank@ubuntu:~/0x03$ cat 8-main.py
#!/usr/bin/python3
multiple_returns = __import__(&#39;8-multiple_returns&#39;).multiple_returns

sentence = &quot;At school, I learnt C!&quot;
length, first = multiple_returns(sentence)
print(&quot;Length: {:d} - First character: {}&quot;.format(length, first))

frank@ubuntu:~/0x03$ ./8-main.py
Length: 22 - First character: A
frank@ubuntu:~/0x03$ 
</code></pre>

<h3>9. Find the max</h3>
<p>Write a function that finds the biggest integer of a list. </p>

<ul>
<li>Prototype: <code>def max_integer(my_list=[]):</code></li>
<li>If the list is empty, return <code>None</code></li>
<li>You can assume that the list only contains integers</li>
<li>You are not allowed to import any module</li>
<li>You are not allowed to use the builtin <code>max()</code></li>
</ul>

<pre><code>frank@ubuntu:~/0x03$ cat 9-main.py
#!/usr/bin/python3
max_integer = __import__(&#39;9-max_integer&#39;).max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print(&quot;Max: {}&quot;.format(max_value))

frank@ubuntu:~/0x03$ ./9-main.py
Max: 90
frank@ubuntu:~/0x03$ 
</code></pre>

<h3>10. Only by 2</h3>
<p>Write a function that finds all multiples of 2 in a list.</p>

<ul>
<li>Prototype: <code>def divisible_by_2(my_list=[]):</code></li>
<li>Return a new list with <code>True</code> or <code>False</code>, depending on whether the integer at the same position in the original list is a multiple of 2</li>
<li>The new list should have the same size as the original list</li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>frank@ubuntu:~/0x03$ cat 10-main.py
#!/usr/bin/python3
divisible_by_2 = __import__(&#39;10-divisible_by_2&#39;).divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i &lt; len(list_result):
    print(&quot;{:d} {:s} divisible by 2&quot;.format(my_list[i], &quot;is&quot; if list_result[i] else &quot;is not&quot;))
    i += 1

frank@ubuntu:~/0x03$ ./10-main.py
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
frank@ubuntu:~/0x03$ 
</code></pre>

<h3>11. Delete at</h3>
<p>Write a function that deletes the item at a specific position in a list.</p>

<ul>
<li>Prototype: <code>def delete_at(my_list=[], idx=0):</code></li>
<li>If <code>idx</code> is negative or out of range, nothing change (returns the same list)</li>
<li>You are not allowed to use <code>pop()</code></li>
<li>You are not allowed to import any module</li>
</ul>

<pre><code>frank@ubuntu:~/0x03$ cat 11-main.py
#!/usr/bin/python3
delete_at = __import__(&#39;11-delete_at&#39;).delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

frank@ubuntu:~/0x03$ ./11-main.py
[1, 2, 3, 5]
[1, 2, 3, 5]
frank@ubuntu:~/0x03$ 
</code></pre>

<h3>12. Switch</h3>
<p>Complete the source code in order to switch value of <code>a</code> and <code>b</code></p>

<ul>
<li>You can find the source code <a href="https://github.com/alx-tools/0x03.py/blob/master/12-switch_py" title="here" target="_blank">here</a></li>
<li>Your code should be inserted where the comment is (line 4)</li>
<li>Your program should be exactly 5 lines long</li>
</ul>

<pre><code>frank@ubuntu:~/py/0x03$ ./12-switch.py
a=10 - b=89
frank@ubuntu:~/py/0x03$ wc -l 12-switch.py
5 12-switch.py
frank@ubuntu:~/py/0x03$ 
</code></pre>

<h3>13. Linked list palindrome</h3>
<p><strong>Technical interview preparation</strong>: </p>

<ul>
<li>You are not allowed to google anything</li>
<li>Whiteboard first</li>
</ul>

<p>Write a function in C that checks if a singly linked list is a palindrome.</p>

<ul>
<li>Prototype: <code>int is_palindrome(listint_t **head);</code></li>
<li>Return: <code>0</code> if it is not a palindrome, <code>1</code> if it is a palindrome</li>
<li>An empty list is considered a palindrome</li>
</ul>

<pre><code>frank@ubuntu:0x03$ cat lists.h 
#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

#endif /* LISTS_H */
frank@ubuntu:0x03$
</code></pre>

<pre><code>frank@ubuntu:0x03$ cat linked_lists.c 
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &quot;lists.h&quot;

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf(&quot;%i\n&quot;, current-&gt;n);
        current = current-&gt;next;
        n++;
    }

    return (n);
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new-&gt;n = n;
    new-&gt;next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current-&gt;next != NULL)
            current = current-&gt;next;
        current-&gt;next = new;
    }

    return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head-&gt;next;
        free(current);
    }
}
frank@ubuntu:0x03$
</code></pre>

<pre><code>frank@ubuntu:0x03$ cat 13-main.c
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &quot;lists.h&quot;

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&amp;head, 1);
    add_nodeint_end(&amp;head, 17);
    add_nodeint_end(&amp;head, 972);
    add_nodeint_end(&amp;head, 50);
    add_nodeint_end(&amp;head, 98);
    add_nodeint_end(&amp;head, 98);
    add_nodeint_end(&amp;head, 50);
    add_nodeint_end(&amp;head, 972);
    add_nodeint_end(&amp;head, 17);
    add_nodeint_end(&amp;head, 1);
    print_listint(head);

    if (is_palindrome(&amp;head) == 1)
        printf(&quot;Linked list is a palindrome\n&quot;);
    else
        printf(&quot;Linked list is not a palindrome\n&quot;);

    free_listint(head);

    return (0);
}
frank@ubuntu:0x03$
</code></pre>

<pre><code>frank@ubuntu:0x03$ gcc -Wall -Werror -Wextra -pedantic 13-main.c linked_lists.c 13-is_palindrome.c -o palindrome
frank@ubuntu:0x03$ ./palindrome
1
17
972
50
98
98
50
972
17
1
Linked list is a palindrome
frank@ubuntu:0x03$
</code></pre>


<h3>14. CPython #0: Python lists</h3>
 <p>CPython is the reference implementation of the Python programming language. Written in C, CPython is the default and most widely used implementation of the language.<br />
Since we now know a bit of C, we can look at what is happening under the hood of Python. Let&rsquo;s have fun with Python and C, and let&rsquo;s look at what makes Python so easy to use.</p>

<ul>
<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS</li>
</ul>

<p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/7e7834b535261d05532fb80a9304f7051c4ad7ac.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230814%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230814T163417Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5f35a93bddf16ae046b13887d3608f066ce111a63dda6050bdd9f4500fa44b75" alt="" loading='lazy' style="" />
<br /><br />
Create a C function that prints some basic info about Python lists.</p>

<ul>
<li>Prototype: <code>void print_python_list_info(PyObject *p);</code></li>
<li>Format: see example</li>
<li>Python version: 3.4</li>
<li>Your shared library will be compiled with this command line: <code>gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c</code></li>
<li>OS: <code>Ubuntu 14.04 LTS</code></li>
<li>Start by reading:

<ul>
<li>listobject.h</li>
<li>object.h</li>
<li><a href="/rltoken/jmRTk4m1VSzjsu3QTGaC6w" title="Common Object Structures" target="_blank">Common Object Structures</a></li>
<li><a href="/rltoken/7V1HlQRESjCqrKrw_O_Urw" title="List Objects" target="_blank">List Objects</a></li>
</ul></li>
</ul>

<pre><code>frank@ubuntu:~/CPython$ gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
frank@ubuntu:~/CPython$ cat 100-test_lists.py 
import ctypes

lib = ctypes.CDLL(&#39;./libPyList.so&#39;)
lib.print_python_list_info.argtypes = [ctypes.py_object]
l = [&#39;hello&#39;, &#39;World&#39;]
lib.print_python_list_info(l)
del l[1]
lib.print_python_list_info(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], &quot;My string&quot;]
lib.print_python_list_info(l)
l = []
lib.print_python_list_info(l)
l.append(0)
lib.print_python_list_info(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list_info(l)
l.pop()
lib.print_python_list_info(l)
frank@ubuntu:~/CPython$ python3 100-test_lists.py 
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: str
Element 1: str
[*] Size of the Python List = 1
[*] Allocated = 2
Element 0: str
[*] Size of the Python List = 7
[*] Allocated = 7
Element 0: str
Element 1: int
Element 2: int
Element 3: float
Element 4: tuple
Element 5: list
Element 6: str
[*] Size of the Python List = 0
[*] Allocated = 0
[*] Size of the Python List = 1
[*] Allocated = 4
Element 0: int
[*] Size of the Python List = 5
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
Element 4: int
[*] Size of the Python List = 4
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
frank@CPython:~/CPython$ 
</code></pre>


