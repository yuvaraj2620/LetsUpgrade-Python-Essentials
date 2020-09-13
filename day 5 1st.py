def matchlist(list=[]):
    sublist = [1, 1, 5]
    for i in range(len(list)):
        if list[i] == sublist[0]:
            for j in range(i + 1, len(list)):
                if list[j] == sublist[1]:
                    for k in range(j + 1, len(list)):
                        if list[k] == sublist[2]:
                            return
                        print("it's a Match")
    else:
        return
    print("it's Gone")


# In[32]:


matchlist([1, 5, 3, 1])

# In[33]:


matchlist([1, 2, 1, 7, 5, 9])

