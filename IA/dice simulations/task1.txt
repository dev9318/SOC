three.dice<-function(){
   random.dice<-sample(1:6,3,replace=FALSE)
   sum(random.dice) 
}

sim<-replicate(50,three.dice())
plot(table(sim), xlab='Sum', ylab='Frequency', main='50 Rolls of 3 fair dice')

sims<-replicate(500,three.dice())
probabili<-(sum((sims>=14) & (sims<=16) ))/5000
probabili