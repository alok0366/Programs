#include<iostream>
#include<unistd.h>
#include<sys/types.h>

using namespace std;
int main(){
	int init;
		init=fork();
		if(init==0){
			cout<<"PARENT PROCESS"<<endl;
			cout<<"process_id"<<getpid()<<"parent process_id"<<getppid()<<endl;
			int login,kthread,sshd;
				login=fork();
				kthread=fork();
				sshd=fork();
			if(login==0){
				int ps,emacs;
				cout<<"process_id"<<getpid()<<"parent process_id"<<getppid()<<endl;
				ps=fork();
				emacs=fork();
				if(ps==0){
					cout<<"process_id"<<getpid()<<"parent process_id"<<getppid()<<endl;
					exit(0);}
				if(emacs==0){
					cout<<"process_id"<<getpid()<<"parent process_id"<<getppid()<<endl;
					exit(0);}
					exit(0);
			}
			if(kthread==0){
				int khelper,pdflush;
				cout<<"process_id"<<getpid()<<"parent process_id"<<getppid()<<endl;
				khelper=fork();
				pdflush=fork();
				if(khelper==0){
					cout<<"process_id"<<getpid()<<"parent process_id"<<getppid()<<endl;
					exit(0);}
				if(pdflush==0){
					cout<<"process_id"<<getpid()<<"parent process_id"<<getppid()<<endl;
					exit(0);}
					exit(0);
				}
			if(sshd==0){
				cout<<"process_id"<<getpid()<<"parent process_id"<<getppid()<<endl;
				int tcsch;
					tcsch=fork();
					if(tcsch==0){
						cout<<"process_id"<<getpid()<<"parent process_id"<<getppid()<<endl;
						exit(0);}}
}
		return 0;
}
