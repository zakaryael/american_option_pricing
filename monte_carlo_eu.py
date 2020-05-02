
import project_option_pricing
from scipy.stats import norm
from math import sqrt
class mc_eu(Option):
    def price(self, n, level = 0.95):
        x = asset.simulate(n)
        y = self.payoff(x)
        delta = np.mean(y)
        Var = np.var(y)
        CI = [delta + q * sqrt(Var/n) for q in norm.interval(level)]
        return {"option price":delta, "confidence interval":CI, "variance":Var}
    
    def evolution(self, n, level = 0.95):
        x = asset.simulate(n)
        y = self.payoff(x)
        nvec = 
        delta = np.cumsum(y) / np.array(range(1, n))
        Var <- ( np.cumsum(y**2) -  * (delta ^ 2)) / 0:(n-1); Var[1] <- 0
        i1 <- delta - q * sqrt (Var / 1:n)
        i2 <- delta + q * sqrt (Var / 1:n)
        t <- 1:n
        plot(t, delta, type = 'l')
        lines(t, i1, col = 'red', type = 'l')
        lines(t, i2, col = 'blue', type = 'l')

market = Market(0, 0.2, 1)
asset = Asset(market, 100)
option = mc_eu(asset, 90, is_put = False, is_american = True)


print("le prix blbalbjaljbal: ", option.price(1000))  