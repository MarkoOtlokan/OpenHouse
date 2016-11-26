#include<stdlib.h>
#include<stdio.h>

struct slog {
   char a;
   struct slog *sledeci;
   int n;
};
typedef struct slog item;

void incijalizacija(item **glava);
void dodavanje(struct slog *glava,char g);
void dodati(struct slog *glava,char g);
struct slog *trazi(char c,struct slog *glava);
void brisati(char t,struct slog *glava);
void brisatisve(struct slog *glava);
void ispisatisve(struct slog *glava);
void dodatibr(struct slog *glava,int h);
item * glava,* token, *brisac;
void prvi();
void drugi();
int main() {
    incijalizacija(glava);
   return 0;
   }

void incijalizacija(item ** glava){
    glava=NULL;
}
void dodavanje(struct slog *glava,char g){
    struct slog *token2;
    token= (item *)malloc(sizeof(item));
    if(glava==NULL){
        glava=token;
    }
    else{
        glava=token2;
        glava->sledeci=token;
    }
    token -> a=g;
    token -> sledeci=token2;
}
void dodati(struct slog *glava,char g){
    struct slog *token2;
    token= (item *)malloc(sizeof(item));
    if(glava==NULL){
        glava=token;

    }
    else{
        token2=glava;
        while(token2->sledeci!=NULL){
            token2=token2->sledeci;
        }
    }
    token2->sledeci=token;
    token-> a=g;
    token -> sledeci=NULL;
}
struct slog *traziti(char c){
    struct slog *pretrazivac1,*pretrazivac2;
    pretrazivac1=glava;
    while(pretrazivac1==NULL){
        if(pretrazivac1->a==c){
            brisac=pretrazivac2;
            return pretrazivac1;
        }
        else{
            pretrazivac2=pretrazivac1;
            pretrazivac1=pretrazivac1->sledeci;
        }
    }
}
void brisati(char t,struct slog *glava){
    struct slog *izbrisati;
    izbrisati=traziti(t);
    if(izbrisati==NULL){
        return;
    }
    else{
        brisac->sledeci=brisac->sledeci->sledeci;
    }
}
void brisatisve(struct slog *glava){
    glava=NULL;
}
void ispisatisve(struct slog *glava){
    struct slog *pretraga;
    pretraga=glava;
    int i=0;
    while(pretraga==NULL){
        i++;
        printf("%c",pretraga->a);
        pretraga=pretraga->sledeci;
    }
    printf("%i",i);
}
prvi(){
    char t='';
    while(1){
        scanf("%c",t);
        if(t=='.'){
            break;
        }
        else{
            dodavanje(glava,t);
        }
    ispisatisve(glava);
    }
}
void dodatibr(struct slog *glava,int h){
    struct slog *token2;
    token= (item *)malloc(sizeof(item));
    if(glava==NULL){
        glava=token;

    }
    else{
        token2=glava;
        while(token2->sledeci!=NULL){
            token2=token2->sledeci;
        }
    }
    token2->sledeci=token;
    token-> n=h;
    token -> sledeci=NULL;
}
void drugi(){
    int n,i;
    struct slog *goken;
    goken=glava;
    scanf("%i",&n);
    for(i=0;i<n;i++){
        dodatibr(glava,n);
    }
    for(i=0;i<n;i++){
        goken->n++;
        goken=goken->sledeci;
    }
    ispisatisve(glava);
}
void treci(){

}
