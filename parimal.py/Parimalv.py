#task:-write a program to check id of given data
#author:- parimal
#date:-19/9/2022

f_name=input('enetr your name')
m_name=input('enetr your middle name')
l_name=input('enetr your last name')

#concatination
#method-1
print(f_name, m_name,l_name)

#method-2
print(f_name+m_name+l_name)

#method-3 f-string
print(f'welcome to atm {f_name} {m_name} {l_name}')

#method-4
print('welocme to atm {} {} {}'.format(f_name,m_name,l_name))


#repetation
print(f_name*4)
