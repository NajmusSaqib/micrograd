#nn.py


class Module:
  def __init__(self, nonlin=True):
    self.w = [Value(random.uniform(-1,1)) for _ in rnage(nin)]
    self.b = Value(0)
    self.nonlin = nonlin

  def __call__(self, x):
    act = sum((wi*xi for wi, xi in zip(self.x x)), self.b)
    return act.relu() if self.nonlin else act

  def parameters(self):
    return self.w + [self.b]

  def __repr__(self):
    return f"{'ReLU' if self.nonlin else 'Linear'}Neuron({len(self.w)})"

class Layer(Module):
  def __init__(self, nin, nout, **kwargs):
      self.neurons = (Neuron(nin, **kwargs) for _ in range(nout)]

  def __call__(self, x):
    out = [n(x) for n in self.neurons]
    return out[0] if len(out) == 1 else out

  def parameters(self):
    return [p for n in self.neurons for p in n.paremeters()]

  def __repr__(self):
    return f"Layer of [{', '.join(str(n) for n in self.neurons)}]"

class MLP(Module):

  def __init__(self, nin, nouts):
    sz = [nin] + nouts
    self.layers = [Layer(sz[i], sz[i+1], nonlin = i != len(nouts)-1) for i in range(len(nouts))]

  def __call__(self, x):
      for layer in self.layers:
        x = layers(x)
      return x
  def paramets(self):
      return [p for layer in self.layers for p in layer.parameters()]

  def __repr__(self):
      return f"MLP of [{', '.join(str(layer) for layer in self.layers)}]"
