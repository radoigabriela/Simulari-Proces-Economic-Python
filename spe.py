1
import simpy
import random
def generator_client(env, coada):
    while True:
        yield env.timeout(random.uniform(2, 5))  
        env.process(client(env, coada))  
def client(env, coada):
    with coada.request() as req:
        yield req  
        timp_servire = random.uniform(3, 6) 
        yield env.timeout(timp_servire)  
        print(f"Timpul {env.now}: Clientul a fost servit după {timp_servire:.2f} minute.")
def monitorizare_clienti(env, coada):
    while True:
        print(f"Timpul {env.now}: A sosit un nou client.")
        yield env.timeout(1)  
env = simpy.Environment()
coada = simpy.Resource(env, capacity=1)  
env.process(generator_client(env, coada))
env.process(monitorizare_clienti(env, coada))
env.run(until=15)




2
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
def evolutie_populatie(t, y):
    alpha = 0.1  
    beta = 0.02  
    return alpha * y - beta * y**2
t_span = (1925, 2025)
y0 = [10]  
sol = solve_ivp(evolutie_populatie, t_span, y0, t_eval=np.linspace(1925, 2025, 1000))
plt.plot(sol.t, sol.y[0], label='Populație')
plt.xlabel
plt.ylabel
plt.title
plt.grid(True)
plt.legend()
plt.show()




3
import numpy as np
numar_aruncari = 50
aruncari_zar = np.random.randint(1, 13, size=numar_aruncari)
sumele_aruncari = np.cumsum(aruncari_zar)
print("Sumele primelor 5 aruncări de zar cu 12 fețe:")
print(sumele_aruncari[:5])



4
import numpy as np
numar_perioade = 50 
coeficient_autoregresie = 0.9  
medie = 0  
deviatie_standard = 1.2  
temperatura = [np.random.normal(loc=medie, scale=deviatie_standard)]
for i in range(1, numar_perioade):
    temperatura_noua = coeficient_autoregresie * temperatura[-1] + np.random.normal(loc=medie, scale=deviatie_standard)
    temperatura.append(temperatura_noua)
print("Evoluția temperaturii medii anuale pe o perioadă de 50 de ani:")
print(temperatura)



5
import numpy as np
numar_participanti = 50  
timp_mediu = 12 
deviatia_standard = 3  
timp_participanti = np.random.normal(loc=timp_mediu, 
scale=deviatia_standard,
size=numar_participanti)
print("Primii 5 timpi generaţi pentru participanți:")
print(timp_participanti[:5])




6
import simpy
import numpy as np
def generare_timp():
    return np.random.exponential(1.5)  
def procesare_cerere(env, numar_cereri, coada):
    for i in range(numar_cereri):
        yield env.timeout(generare_timp())  
        with coada.request() as req:
            yield req
            yield env.timeout(generare_timp())  
env = simpy.Environment()
coada = simpy.Resource(env, capacity=1)  
env.process(procesare_cerere(env, numar_cereri=10, coada=coada))
env.run()
print("Simularea cozii a fost completă.")



7
import simpy
import random
def client(env, server):
    arrival_time = env.now
    print(f"Sosirea clientului la timpul {arrival_time:.2f}")
    with server.request() as request:
        yield request
        service_time = random.expovariate(1.0 / SERVICE_RATE)
        yield env.timeout(service_time)
        departure_time = env.now
        print(f"Plecare clientului la timpul {departure_time:.2f}, după un serviciu de {service_time:.2f}")
SERVICE_RATE = 3.0  
env = simpy.Environment()
server = simpy.Resource(env, capacity=1)
for i in range(5):
    env.process(client(env, server))
env.run()



8
class Agent:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def move(self, new_position):
        self.position = new_position
class Environment:
       def __init__(self, width, height):
              self.width = width
              self.height = height
              self.grid = [[None for _ in range(width)] for _ in range(height)]
       def add_agent(self, agent, position):
              x, y = position
              self.grid[y][x] = agent
       def remove_agent(self, agent):
              for row in self.grid:
                     if agent in row:
                            row.remove(agent)
       def move_agent(self, agent, new_position):
              self.remove_agent(agent)
              agent.move(new_position)
              self.add_agent(agent, new_position)
env = Environment(10, 10)
agent1 = Agent("Agent1", (0, 0))
env.add_agent(agent1, (0, 0))
print("Mediul cu agent adăugat:")
for row in env.grid:
       print(row)
class Worker(Agent):
       def __init__(self, name, position, wage):
              super().__init__(name, position)
              self.wage = wage
       def find_job(self, job_market):
              pass
class Employer(Agent):
       def __init__(self, name, position, wage):
              super().__init__(name, position)
              self.wage = wage
       def post_job(self, job_market):
              pass
class JobMarket(Environment):
       def __init__(self, width, height):
              super().__init__(width, height)
              self.workers = []
              self.employers = []
       def add_worker(self, worker):
              self.workers.append(worker)
              self.add_agent(worker, worker.position)
       def add_employer(self, employer):
              self.employers.append(employer)
              self.add_agent(employer, employer.position)
job_market = JobMarket(10, 10)
worker1 = Worker("Worker1", (0, 0), 10)
employer1 = Employer("Employer1", (5, 5), 20)
job_market.add_worker(worker1)
job_market.add_employer(employer1)
print("Mediul cu lucrătorii și angajatorii adăugați:")
for row in job_market.grid:
       print(row)



9
class Agent:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def move(self, new_position):
        self.position = new_position
    def __repr__(self):
        return f"<__main__.Agent object at {hex(id(self))}>"
class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
    def add_agent(self, agent, position):
        x, y = position
        self.grid[y][x] = agent
    def remove_agent(self, agent):
        for row in self.grid:
            if agent in row:
                row.remove(agent)
    def move_agent(self, agent, new_position):
        self.remove_agent(agent)
        agent.move(new_position)
        self.add_agent(agent, new_position)
class Firm(Agent):
       def __init__(self, name, position, market_share):
              super().__init__(name, position)
              self.market_share = market_share
       def adjust_price(self, market_demand):
              adjusted_price = 10 * self.market_share * market_demand / 100  
              print(f"Firma {self.name} ajustează prețul la:  {adjusted_price}")
class Market(Environment):
       def __init__(self, width, height, firms):
              super().__init__(width, height)
              self.firms = firms
       def update(self):
              market_demand = self.calculate_demand()
              for firm in self.firms:
                     firm.adjust_price(market_demand)
       def calculate_demand(self):
              total_demand = sum(10 - firm.market_share * 5 for firm in self.firms)
              return total_demand
firm1 = Firm("Firm1", (0, 0), 0.2)
firm2 = Firm("Firm2", (1, 1), 0.3)
market = Market(10, 10, [firm1, firm2])
for _ in range(5):
       market.update()



10
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import matplotlib.pyplot as plt
import random
class CarAgent(Agent):
    def __init__(self, unique_id, model, destination):
        super().__init__(unique_id, model)
        self.speed = 1  
        self.destination = destination  
        self.type = "Residential" if random.random() < 0.5 else "Commercial"  
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        new_position = random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
    def step(self):
        self.move()
class IntersectionAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.traffic_light = "Red" 

    def step(self):
        nearby_cars = self.model.grid.get_neighbors(self.pos, moore=False, include_center=False)
        if len(nearby_cars) > 3:  
            self.traffic_light = "Green"
        else:
            self.traffic_light = "Red"
        if self.traffic_light == "Red":
            for car in nearby_cars:
                car.speed = 0
        else:
            for car in nearby_cars:
                car.speed = 1  
class TrafficModel(Model):
    def __init__(self, width, height, num_cars, num_intersections):
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        for i in range(num_cars):
            destination = random.choice(["Residential", "Commercial"])
            car = CarAgent(i, self, destination)
            self.schedule.add(car)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(car, (x, y))
        for i in range(num_intersections):
            intersection = IntersectionAgent(i + num_cars, self)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(intersection, (x, y))
            self.schedule.add(intersection)
        self.datacollector = DataCollector(
            agent_reporters={"Speed": lambda a: getattr(a, 'speed', None)}
        )
    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
model = TrafficModel(width=10, height=10, num_cars=30, num_intersections=4)
for _ in range(100):
    model.step()
data = model.datacollector.get_agent_vars_dataframe()
average_speed = data.groupby('Step')['Speed'].mean()
plt.figure(figsize=(10, 6))
plt.plot(average_speed.index, average_speed.values, marker='o', linestyle='-')
plt.title('Evoluția Vitezei Medii a Mașinilor în Timp')
plt.xlabel('Pas de timp')
plt.ylabel('Viteză medie')
plt.grid(True)
plt.show()
def calculate_intersection_density(model):
    intersection_density = {}
    for intersection in model.schedule.agents:
        intersection_density[intersection.unique_id] = len(model.grid.get_cell_list_contents([intersection.pos]))
    return intersection_density
