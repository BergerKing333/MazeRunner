import noise
import numpy as np
import matplotlib.pyplot as plt

# Parameters for noise generation
shape = (512, 512)
scale = 25.0
octaves = 1
persistence = 0.5
lacunarity = 2.0

# Generate Perlin noise
noise_array = np.zeros(shape)
for i in range(shape[0]):
    for j in range(shape[1]):
        noise_array[i][j] = noise.pnoise2(i / scale, 
                                          j / scale, 
                                          octaves=octaves, 
                                          persistence=persistence, 
                                          lacunarity=lacunarity)

# Plot the noise
plt.imshow(noise_array, cmap='gray')
plt.colorbar()
plt.show()