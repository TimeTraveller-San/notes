# Activation functions
Activations functions are used to introduce non-linearity in neural networks which allows them to learn interesting things other than simple linear mulitplications. There are several activation functions and have their own uses:

## Sigmoid 
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/9537e778e229470d85a68ee0b099c08298a1a3f6)
- Output ranges between 0 and 1
- Derivative ranges between 0 and ~0.25
- Because of it's output range it is used to make gates in LSTMs and GRUs. A value of 0 means let no info pass while a value of 1 means let all the info pass
- Since maximum of gradient is very less it converges slowly (becuase small updates are made in weights)
- Lower magnitude of gradient also introduces the problem of vanishing gradients in deep neural networks and RNNs
- It's gradient calculation is computationally slower than tanh and relu

## Tanh 
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/b8dc4c309a551cafc2ce5c883c924ecd87664b0f)
- Output ranges between -1 and 1
- Derivative ranges between 0 and 1
- Here's a comparison graph:
![](https://theclevermachine.files.wordpress.com/2014/09/nnet-error-functions2.png)
- tanh gradient is computationally easier to compute
- tanh gradient has a magnitude larger than sigmoid. It does suffer the vanishing gradient problem but much less than sigmoid
- Since magnitude of gradient is larger it converges faster than sigmoid

## RELU
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/bb2c32931fad595832c8e66f2f73760ebcbc0096)
- Output varies between 0 and +infinity
- Gradient is either 0 or 1
- Suffers no vanishing gradient problem
- For negative input gradient is zero which kills the neuron and allows no further computation over it

## Leaky RELU
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/01d5ac8361d825fe42fbde1ed42047aeac1e6160)
- Same as RELU but gives a little weight to negative input to prevent it from dying

## Parametric RELU
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/6883e7bff0d9ac2f89caa6c905be539bf7c13d65)
a < 1
- Same as leaky RELU but converts the earlier coeffecient (0.001) to a parameter that can be learned by the network.

## Softmax
hj=ezj / ∑ezi
- Calculates probability distribution of a value over all other values
- Output of each value ranges between 0 and 1 (probability)
- Sum of all outputs is 1

