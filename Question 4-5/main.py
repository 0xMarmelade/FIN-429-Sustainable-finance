import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from pypfopt import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
from pypfopt import plotting


firms = pd.read_excel('https://github.com/0xMarmelade/FIN-429-Sustainable-finance/raw/main/firm_names.xlsx')
scores = pd.read_excel('https://github.com/0xMarmelade/FIN-429-Sustainable-finance/raw/main/Soc.xlsx', index_col = 0)
returns = pd.read_excel('https://github.com/0xMarmelade/FIN-429-Sustainable-finance/raw/main/monthlyreturns.xlsx', index_col = 0)
eu_countrycodes = ['AL','AD', 'AM','AT','BA','BE','BG','CH','CY','DE','DK','EE','ES','FI','FR','GE', 'GB','GR','HR','HU','IE','IS','IT','LT','LV','MC','MK','MT','NL','NO','PL','PT','RO','RS', 'RU','SE','SI', 'TR', 'UA', 'MD', 'LI']

'''Transposing table to get firms as rows, reset columns to dates'''

scores = scores.transpose()
scores.index.rename('ISIN', inplace=True)

firms.set_index("ISIN", inplace=True)

'''Join Social scores to firm's names and locations Filter on firms that are located in Europe'''

scores = scores.join(firms, how="left", on="ISIN")
scores = scores[scores["Country"].isin(eu_countrycodes)]

scores.dropna(how='all', axis='columns', inplace=True)

eu_firm_returns = returns[scores.index]

#select 50 random companies
eu_firm_returns_50= eu_firm_returns.sample(n=50,axis='columns')

print(eu_firm_returns_50)

#compute their log return, as it will be easier to do computations with

#eu_firm_returns_50_log=np.log(eu_firm_returns_50)

#eu_firm_returns_50_mean=eu_firm_returns_50.mean()
#cov_matr= risk_models.sample_cov(eu_firm_returns_50)
#print(cov_matr)



annualized_ret=eu_firm_returns_50.mean()*12
print(np.mean(annualized_ret))
cov_matr=eu_firm_returns_50.cov()
#print(cov_matr)
ef= EfficientFrontier(annualized_ret,cov_matr)
ef.min_volatility()



expected_returns.mean_historical_return()
'''
ef.min_volatility()
weightsss = ef.clean_weights()
print(weightsss)
'''



#eu_firm_returns_50_cov= eu_firm_returns_50_mean.cov()

#print(eu_firm_returns_50_mean)
#we create random vectors of weigths for the 50 different assets
def weigthcreator(re):
    rand = np.random.random(len(re.columns))
    rand /= rand.sum(rand)
    rand= np.round(rand,3)
    return rand


# we compute the return for the given set of weigths
'''
 portfolio_return= (Weigths) dot_product (mean of log returns)
 
because the returns are in log the mean function will also give the annualized return  
'''
#print(eu_firm_returns_50_log.mean())
def totalreturn(w):
    return np.dot(eu_firm_returns_50.mean(),w)*12 #we annualize them by multiplying by 12 as we have monthly returns

def annualized_return(portfolio_return):
    return portfolio_return.mean() * 12

def portfoliostd(w):
    return np.dot(np.dot(eu_firm_returns_50_mean.cov(),w),w)**(1/2)*np.sqrt(12)


#Now we compute the returns for a bunch of random weights to visualize the efficient frontier
portfolio_returns= [] # list that will contain the total returns of the portfolios
portfolio_std=[] #list that will contain the standard deviation or risk
portfolio_weigths=[] # list with all the different set of random weigths
sharpe_ratio= []
portfolio_risks=[]
weigths=[] #initiate weigth vector
RF=0
'''
    
weigths=weigthcreator(eu_firm_returns_50_log)
print(weigths)
returns_plot.append(totalreturn(weigths))
stds.append(portfoliostd(weigths))
print(stds)
we.append(weigths)
'''


'''
for i in range(500):
    weigths=weigthcreator(eu_firm_returns_50)
    returns_plot.append(totalreturn(weigths))
    stds.append(portfoliostd(weigths))
    we.append(weigths)

plt.scatter(stds,returns_plot)
plt.show()

'''

for portfolio in range(1000):
    #Create random weigths
    weigths= np.random.random_sample(len(eu_firm_returns_50.columns))
    weigths= np.round((weigths/np.sum(weigths)),3)
    portfolio_weigths.append(weigths)
    #annualized returns
    #annualized_returns= np.sum(eu_firm_returns_50.mean()*weigths)*12
    #annualized_returns = np.dot(eu_firm_returns_50.mean(), weigths) * 12
    annualized_returns = np.mean(eu_firm_returns_50.mean()*weigths*12)
    portfolio_returns.append(annualized_returns)
    #covariance & portfolio risk
    matrix_covariance=eu_firm_returns_50.cov()* 12
    portfolio_variance= np.dot(weigths.T,np.dot(matrix_covariance,weigths))
    portfolio_std=np.sqrt(portfolio_variance)
    portfolio_risks.append(portfolio_std)
    #sharpe ratio
    #sharpe_ratio=(annualized_returns-RF )/portfolio_std
    #sharpe_ratio.append(sharpe_ratio)

#print(np.mean(eu_firm_returns_50.mean()*weigths*12))
#print(portfolio_risks)
portfolio_returns=np.array(portfolio_returns)
portfolio_risks=np.array(portfolio_risks)
#sharpe_ratio=np.array(sharpe_ratio)

#portfolio_metrics=[portfolio_returns,portfolio_risks,sharpe_ratio,portfolio_weigths]
portfolio_metrics=[portfolio_returns,portfolio_risks,portfolio_weigths]

portfolio_df=pd.DataFrame(portfolio_metrics).T
portfolio_df.columns=['Return','Risk','Weights']

#print(expected_returns.mean_historical_return(eu_firm_returns_50))
#print(portfolio_returns)
#print(portfolio_risks)

plt.scatter(portfolio_risks,portfolio_returns, c =portfolio_returns/portfolio_risks)
plt.show()