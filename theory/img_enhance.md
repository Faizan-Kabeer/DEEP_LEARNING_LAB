# Image Enhancement 🖼️

## Table of Contents
* Histogram Equalization
* Morphological Operations

---

## Histogram Equalization

Histogram Equalization is a technique used to improve the global contrast of an image. It works by "spreading out" the most frequent pixel intensity values to cover a wider, more uniform range of the intensity scale. The main goal is to create an output image with a "flatter" histogram. This process typically reveals details in parts of the image that were previously too dark or too bright.



### The Equations

The transformation is driven by the image's Cumulative Distribution Function (CDF).

#### 1. The Ideal Formula

This formula is the direct mathematical concept. It scales the CDF directly to the maximum output value.

$$s_k = (L - 1) \times \text{CDF}(r_k)$$

* **$s_k$**: The new, output pixel value.
* **$L - 1$**: The maximum possible intensity (e.g., 255 for an 8-bit image).
* **$r_k$**: The original pixel value.
* **$\text{CDF}(r_k)$**: The normalized CDF (a value from 0 to 1). It's the sum of probabilities of all intensities from 0 up to $r_k$.

#### 2. The Practical Formula

This is the version most software libraries (like OpenCV) actually use. It's more robust because it stretches the actual pixel range found in the image to fill the entire possible output range (e.g., 0 to 255).

$$s_k = \text{round} \left( \frac{\text{CDF-count}(r_k) - \text{CDF}_{\text{min}}}{(M \times N) - \text{CDF}_{\text{min}}} \times (L - 1) \right)$$

* **$\text{CDF-count}(r_k)$**: The raw count of pixels with an intensity less than or equal to $r_k$.
* **$\text{CDF}_{\text{min}}$**: The CDF count of the dimmest pixel that actually exists in the image (i.e., the first non-zero value in the histogram).
* **$M \times N$**: The total number of pixels in the image (Width $\times$ Height).
* **$(L - 1)$**: The maximum pixel value (e.g., 255).

This practical formula guarantees that the image's darkest existing pixel maps to 0 and its brightest existing pixel maps to $(L-1)$, achieving a full-range contrast stretch.

---

## Morphological Operations

Morphological Operations are a set of non-linear operations that process images based on shapes. These techniques probe an image with a small binary pattern called a structuring element (or kernel) to see how it fits or interacts with the pixel neighborhoods.

These operations are essential for tasks like noise removal, boundary extraction, and separating image parts. Some of the operations are:

* **Erosion:** Erosion shrinks the boundaries of the white (foreground) objects. Think of it as "eroding" the edges.

* **Dilation:** Dilation expands the boundaries of the white objects. It's the exact opposite of erosion.

* **Opening:** Opening is just Erosion first, then Dilation.

* **Closing:** Closing is the opposite: Dilation first, then Erosion.