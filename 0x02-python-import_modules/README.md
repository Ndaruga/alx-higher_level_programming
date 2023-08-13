# 0x02. Python - import & modules
<ul>
<li><code>python3</code></li>
</ul>

<h2>Learning Objectives</h2>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome</li>
<li>How to import functions from another file</li>
<li>How to use imported functions</li>
<li>How to create a module</li>
<li>How to use the built-in function <code>dir()</code></li>
<li>How to prevent code in your script from being executed when imported</li>
<li>How to use command line arguments with your Python programs</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version <code>2.8.*</code>)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

  </div>
</div>
<br>

<h1>Tasks</h1>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Import a simple function from a simple file
    </h3>

<p>Write a program that imports the function <code>def add(a, b):</code> from the file <code>add_0.py</code> and prints the result of the addition <code>1 + 2 = 3</code></p>

<ul>
<li>You have to use <code>print</code> function with string format to display integers</li>
<li>You have to assign:

<ul>
<li>the value <code>1</code> to a variable called <code>a</code> </li>
<li>the value <code>2</code> to a variable called <code>b</code></li>
<li>and use those two variables as arguments when calling the functions <code>add</code> and <code>print</code></li>
</ul></li>
<li><code>a</code> and <code>b</code> must be defined in 2 different lines: <code>a = 1</code> and another <code>b = 2</code></li>
<li>Your program should print: <code>&lt;a value&gt; + &lt;b value&gt; = &lt;add(a, b) value&gt;</code> followed with a new line</li>
<li>You can only use the word <code>add_0</code> once in your code</li>
<li>You are not allowed to use <code>*</code> for importing or <code>__import__</code></li>
<li>Your code should not be executed when imported - by using <code>__import__</code>, like the example below</li>
</ul>

<pre><code>frank@ubuntu:~/0x02$ cat add_0.py
#!/usr/bin/python3
def add(a, b):
    &quot;&quot;&quot;My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    &quot;&quot;&quot;
    return (a + b)

frank@ubuntu:~/0x02$ ./0-add.py
1 + 2 = 3
frank@ubuntu:~/0x02$ cat 0-import_add.py
__import__(&quot;0-add&quot;)
frank@ubuntu:~/0x02$ python3 0-import_add.py 
frank@ubuntu:~/0x02$ 
</code></pre>
</div>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. My first toolbox!
    </h3>

<p>Write a program that imports functions from the file <code>calculator_1.py</code>, does some Maths, and prints the result.</p>

<ul>
<li>Do not use the function <code>print</code> (with string format to display integers) more than 4 times </li>
<li>You have to define:

<ul>
<li>the value <code>10</code> to a variable <code>a</code></li>
<li>the value <code>5</code> to a variable <code>b</code></li>
<li>and use those two variables only, as arguments when calling functions (including <code>print</code>)</li>
</ul></li>
<li><code>a</code> and <code>b</code> must be defined in 2 different lines: <code>a = 10</code> and another <code>b = 5</code></li>
<li>Your program should call each of the imported functions. See example below for format</li>
<li>the word <code>calculator_1</code> should be used only once in your file</li>
<li>You are not allowed to use <code>*</code> for importing or <code>__import__</code></li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>frank@ubuntu:~/0x02$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    &quot;&quot;&quot;My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    &quot;&quot;&quot;
    return (a + b)


def sub(a, b):
    &quot;&quot;&quot;My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    &quot;&quot;&quot;
    return (a - b)


def mul(a, b):
    &quot;&quot;&quot;My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    &quot;&quot;&quot;
    return (a * b)


def div(a, b):
    &quot;&quot;&quot;My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    &quot;&quot;&quot;
    return int(a / b)

frank@ubuntu:~/0x02$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
frank@ubuntu:~/0x02$
</code></pre>

  </div>
  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. How to make a script dynamic!
    </h3>

  <div class="panel-body">
    <span id="user_id" data-id="335548"></span>

<p>Write a program that prints the number of and the list of its arguments.</p>

<ul>
<li>The output should be:

<ul>
<li>Number of argument(s) followed by <code>argument</code> (if number is one) or <code>arguments</code> (otherwise), followed by</li>
<li><code>:</code> (or <code>.</code> if no arguments were passed) followed by</li>
<li>a new line, followed by (if at least one argument),</li>
<li>one line per argument:

<ul>
<li>the position of the argument (starting at <code>1</code>) followed by <code>:</code>, followed by the argument value and a new line</li>
</ul></li>
</ul></li>
<li>Your code should not be executed when imported</li>
<li>The number of elements of <code>argv</code> can be retrieved by using: <code>len(argv)</code></li>
<li>You do not have to fully understand lists yet, but imagine that <code>argv</code> can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.</li>
</ul>

<pre><code>frank@ubuntu:~/0x02$ ./2-args.py 
0 arguments.
frank@ubuntu:~/0x02$ ./2-args.py Hello
1 argument:
1: Hello
frank@ubuntu:~/0x02$ ./2-args.py Hello Welcome To The Best School
6 arguments:
1: Hello
2: Welcome
3: To
4: The
5: Best
6: School
frank@ubuntu:~/0x02$ 
</code></pre>

  </div>

<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Infinite addition
    </h3>

<p>Write a program that prints the result of the addition of all arguments</p>

<ul>
<li>The output should be the result of the addition of all arguments, followed by a new line</li>
<li>You can cast arguments into integers by using <code>int()</code> (you can assume that all arguments can be casted into integers)</li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>frank@ubuntu:~/0x02$ ./3-infinite_add.py
0
frank@ubuntu:~/0x02$ ./3-infinite_add.py 79 10
89
frank@ubuntu:~/0x02$ ./3-infinite_add.py 79 10 -40 -300 89 
-162
frank@ubuntu:~/0x02$ 
</code></pre>

<p>Last but not least, your program should also handle big numbers. And the good news is: if your program works for the above example, it will work for the following example:</p>

<pre><code>frank@ubuntu:~/0x02$ ./3-infinite_add.py 1111111111111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999990000000000000000000 11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334567788888899999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334568900000011111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999989999999999999999999
frank@ubuntu:~/0x02$
</code></pre>

<p>Remember how you did (or did not) do it in C? <code>#pythoniscool</code></p>

<p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/621c6dd72e1acff708141f3fab6dfa6ff37c5ee6.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230813%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230813T031420Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a8f991341ca9b1a42087b5aa23ac8bb79433b2fe6097277c7b207e3511ada200" alt="" loading='lazy' style="" /></p>

  </div>
<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Who are you?
    </h3>

<p>Write a program that prints all the names defined by the compiled module <a href="https://github.com/alx-tools/0x02.py/raw/master/hidden_4.pyc" title="hidden_4.pyc" target="_blank">hidden_4.pyc</a> (please download it locally).</p>

<ul>
<li>You should print one name per line, in alpha order</li>
<li>You should print only names that do <strong>not</strong> start with <code>__</code></li>
<li>Your code should not be executed when imported</li>
<li>Make sure you are running your code in Python3.8.x (<code>hidden_4.pyc</code> has been compiled with this version)</li>
</ul>

<pre><code>frank@ubuntu:~/0x02$ curl -Lso &quot;hidden_4.pyc&quot; &quot;https://github.com/alx-tools/0x02.py/raw/master/hidden_4.pyc&quot;
frank@ubuntu:~/0x02$ ./4-hidden_discovery.py | sort
my_secret_santa
print_hidden
print_school
frank@ubuntu:~/0x02$ 
</code></pre>

  </div>
<div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      5. Everything can be imported
    </h3>

<p>Write a program that imports the variable <code>a</code> from the file <code>variable_load_5.py</code> and prints its value.</p>

<ul>
<li>You are not allowed to use <code>*</code> for importing or <code>__import__</code></li>
<li>Your code should not be executed when imported</li>
</ul>

<pre><code>frank@ubuntu:~/0x02$ cat variable_load_5.py
#!/usr/bin/python3
a = 98
&quot;&quot;&quot;Simple variable
&quot;&quot;&quot;

frank@ubuntu:~/0x02$ ./5-variable_load.py
98
frank@ubuntu:~/0x02$
</code></pre>

  </div>
