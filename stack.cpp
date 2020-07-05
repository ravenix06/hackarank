#include<iostream>
#include<bits/stdc++.h>
#include<stack>

using namespace std;
using std::stack;




void showstack(stack<int>s)
{
    while(!s.empty())
	{
		cout <<'\t' <<s.top();
		s.pop();
	}
	cout<<'\n';
	
}

int main()
{
	stack<int>s;
	s.push(10);
	s.push(30);
	s.push(20);
	s.push(5);
	
	cout<<"the stack is:";
	showstack(s);
	
	cout << "\ns.size() : "<< s.size();
	cout<< "\ns.top() : "<< s.top();
	
	cout << "\ns.pop() : ";
	s.pop();
	showstack(s);
	
	return 0;
	
}
