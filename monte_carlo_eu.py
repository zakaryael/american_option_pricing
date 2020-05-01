
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
    

market = Market(0, 0.2, 1)
asset = Asset(market, 100)
option = mc_eu(asset, 90, is_put = False, is_american = True)


print("le prix blbalbjaljbal: ", option.price(1000))  