# Building a Neural Network From Scratch

I will be following the guide from **Aadil Mallick** from *Medium*: 

https://medium.com/@waadlingaadil/learn-to-build-a-neural-network-from-scratch-yes-really-cac4ca457efc 

---

# Sections: 

- Fundamentals: 
    - What is machine learning?
    - Crash course on Matrices. 
    - crash course on derivatives. 
    - crash course on partial derivatives. 
- The Perceptron Model
- Basic Neural Network Notation. 
- Feed Forward. 
- Vectorisation. 
- Cost. 
- Backpropagation. 
- Build That Network. 

---

# What is Machine Learning?

**How Did I Classify Things As A Baby?**
- growing up, if you only saw one breed of dog, probably think other breeds of dogs aren't dogs until told so. 
- if you only say Border Collies then was presented a chihuahua one day, you'd have to expand your definition of what a dog was. 
- Expanded knowledge due to more data. 
- This is how Machines Learn. 
- if you gave the computer a picture of Richard Dean Anderson and told it he was a human, it would only know of one human in the whole world. 
- however, if you gave a computer 100,000 pictures of people and classified them as humans, it would do better. 
- similarly, if you give a computer a banana and called it an 'apple' it would think all apples are bananas wrongly so. 
- to correct this, tell it that the 'banana' is not an apple and actually a 'banana' (enough times) and it will learn. 

To condense: 
there are three steps to Machine Learning. 

1) Gather correctly labelled data. 
2) Create a metric to describe how much error the machine makes when trying to predict what something is. 
3) Iteratively train to reduce the error. 

This leads to **Cost Intuition**. 

When you first use a machine for machine learning, the predictions it makes are usually very wrong, so we correct those mistakes
like how we would teach a child. 
- tell them how they are wrong
- call this the **cost** of the model. 

How does this work?
- say we train a model to classify cats and dogs. 
- give it all images of dogs, but it returns cats for all of them 
- it go $0/3$ correct. 
- quantify rate of errors through cost. 

$$ cost = \frac{\text{number of errors}}{\text{total number of predictions}} $$

**Low Cost = Good Model, High Cost = Bad Model**. 

Lets take a break to try to understand and draw some sort of analogy to neural networks. 

As the name implies, nueral networks are trying to copy what the human brain does. We are trying to imitate how a the brain **thinks** in a form of **Artificial Intelligence**. 
- a human brain has 100 billion **neurons**
- a neural network will have 100 billion **parameters**

---

# Matrices

These are a concise way to represent a system of equations. 
For example, we can represent the complex equation of 

$$
(2 \cdot 1) + (3 \cdot 5) + (2 \cdot 2)
$$
as 
$$ 
[2 \ 3 \ 2] \cdot [1 \ 5\ 2]
$$

- matrix multiplication works as `row x col`

$$
\begin{align}
\begin{pmatrix}
2 & 3 \\ 
4 & 5
\end{pmatrix}
\cdot 
\begin{pmatrix}
5 & 6 \\ 
7 & 8
\end{pmatrix}
& = 
\begin{pmatrix}
(2 \cdot 5 + 3 \cdot 7)
& 
(2 \cdot 6 + 3 \cdot 8) \\
(4 \cdot 5 + 5 \cdot 7) 
& 
(4 \cdot 6 + 5 \cdot 8)
\end{pmatrix}
\\
&= 
\begin{pmatrix} 
31 & 36 \\
55 & 64
\end{pmatrix}
\end{align}
$$

- should always end up with an `r x c` dimensional matrix when matrix multiplying. 
- **Note:** order matters when multiplying matrices. 
- within maching learning, the order to multiply matrices can be very confusing, more important to get the dimensions down correctly. 

**Transposition:**
- transpose an equation by switching around its rows and columns. 
$$
\begin{bmatrix}
5 & 6 \\
7 & 8 \\
9 & 10 
\end{bmatrix} ^ T
= \begin{bmatrix}
5 & 7 & 9 \\
6 & 8 & 10
\end{bmatrix}
$$

- allows us to multiply two matrices together without changing the order. 
- **Law of Transposition**
$$
\begin{align}
W^TX &= XW \\
& \text{Law of Transposition} \\
& \text{} \\
& \text{Proof by example} \\

\text{If, } W &= 
\begin{bmatrix}
1 & 2 \\
3 & 4 
\end{bmatrix}
\text{ and } X = 
\begin{bmatrix}
5 & 7 & 9 \\
6 & 8 & 10
\end{bmatrix}
\\
\text{Then, } \\

\begin{bmatrix}
1 & 2 \\
3 & 4 
\end{bmatrix} ^ T &= 

\begin{bmatrix}
1 & 3 \\
2 & 4 
\end{bmatrix}
\\

\begin{bmatrix}
1 & 3 \\
2 & 4 
\end{bmatrix}

\begin{bmatrix}
5 & 7 & 9 \\
6 & 8 & 10
\end{bmatrix}

&= 

\begin{bmatrix}
23 & 31 & 39 \\
34 & 46 & 58
\end{bmatrix}

\end{align}
$$

