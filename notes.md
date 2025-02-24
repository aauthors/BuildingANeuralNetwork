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