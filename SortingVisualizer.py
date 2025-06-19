import random
import time
import pygame
import heapq

class SortingVisualizer:
    def __init__(self, surf, origin_x, origin_y, width, height, array, maximum, number_of_items, delay=0.02):
        self.surf = surf
        self.x = origin_x
        self.y = origin_y
        self.w = width
        self.h = height
        self.arr = array
        self.maximum = maximum
        self.n = number_of_items
        self.interval_x = self.w / self.n
        self.interval_y = self.h / self.maximum
        self.delay = delay
        self.green_ind = None
        self.red_ind = None
        self.active = True
        self.display()

    def kill_process(self):
        self.active = False

    def display(self):
        pygame.draw.rect(self.surf, (0, 0, 0), (self.x, self.y, self.w, self.h))
        for i in range(self.n):
            col = (255, 255, 255)
            if self.green_ind == i:
                col = (0, 255, 0)
            elif self.red_ind == i:
                col = (255, 0, 0)
            pygame.draw.rect(self.surf, col, (self.x + i * self.interval_x + 1, self.y + self.maximum * self.interval_y - self.arr[i] * self.interval_y, self.interval_x - 2, self.interval_y * self.arr[i]))

    def swap(self, ind1, ind2):
        self.arr[ind1], self.arr[ind2] = self.arr[ind2], self.arr[ind1]

    def wait(self):
        time.sleep(self.delay)

    def bubble_sort(self):
        j = self.n - 1
        while self.active:
            sorte = True
            for i in range(j):
                self.red_ind = i
                self.green_ind = i + 1
                if self.arr[i] > self.arr[i+1]:
                    self.arr[i], self.arr[i+1] = self.arr[i+1], self.arr[i]
                    sorte = False
                self.wait()
            if sorte:
                self.red_ind = self.n - 2
                self.green_ind = self.n - 1
                return
            j -= 1

    def selection_sort(self):
        for i in range(self.n - 1):
            self.red_ind = None
            for j in range(i, self.n):
                if not self.active:
                    return
                if (self.red_ind is None) or (self.arr[self.red_ind] > self.arr[j]):
                    self.red_ind = j
                self.green_ind = j
                self.wait()
            self.swap(self.red_ind, i)

    def insertion_sort(self):
        for i in range(self.n):
            self.green_ind = i + 1
            for j in range(i - 1, -1, -1):
                if not self.active:
                    return
                self.red_ind = j
                if self.arr[j] > self.arr[j+1]:
                    self.swap(j, j+1)
                else:
                    break
                self.wait()
        self.red_ind = self.n - 2
        self.green_ind = self.n - 1

    def overwrite_range(self, left_point, right_point, array):
        n = right_point - left_point
        for i in range(n):
            self.arr[i + left_point] = array[i]
            self.wait()

    def merge_sort(self):
        self.merge_sort_rec(0, self.n)
        self.green_ind = self.n - 1
        self.red_ind = self.n - 2

    def merge_sort_rec(self, left, right):  # Stop before right
        l = right - left
        if l < 2:
            return self.arr[left:right]
        mid = (left + right) // 2
        lefty = self.merge_sort_rec(left, mid)
        righty = self.merge_sort_rec(mid, right)

        left_point = 0
        right_point = 0

        left_n = mid - left
        right_n = right - mid

        while True:
            self.green_ind = left + left_point + right_point
            if left_point >= left_n:
                self.overwrite_range(self.green_ind, right, righty[right_point:])
                return self.arr[left:right]
            if right_point >= right_n:
                self.overwrite_range(self.green_ind, right, lefty[left_point:])
                return self.arr[left:right]
            if lefty[left_point] < righty[right_point]:
                self.arr[self.green_ind] = lefty[left_point]
                left_point += 1
                self.wait()
            else:
                self.arr[self.green_ind] = righty[right_point]
                right_point += 1
                self.wait()

    def quick_sort(self):
        self.quick_sort_rec(0, self.n)
        self.red_ind = self.n - 2
        self.green_ind = self.n - 1

    def quick_sort_rec(self, left, right):
        leny = right - left
        if leny < 2:
            return
        mid_ind = random.randrange(left, right)
        pivot = self.arr[mid_ind]
        self.red_ind = mid_ind
        smaller_than = []
        greater_than = []
        smaller_than_count = 0
        for i in range(left, right):
            if i == mid_ind:
                continue
            item = self.arr[i]
            self.green_ind = i
            if item < pivot:
                smaller_than.append(item)
                smaller_than_count += 1
            else:
                greater_than.append(item)
            self.wait()
        self.overwrite_range(left, smaller_than_count + left, smaller_than)
        self.red_ind = smaller_than_count + left
        self.overwrite_range(smaller_than_count + left, smaller_than_count + left + 1, [pivot])
        self.overwrite_range(smaller_than_count + left + 1, right, greater_than)
        self.quick_sort_rec(left, smaller_than_count + left)
        self.quick_sort_rec(left + smaller_than_count + 1, right)

    def isolate_digit(self, num, pos_from_right_0_indexed):
        return num // (10 ** pos_from_right_0_indexed) % 10

    def radix_sort(self):
        digits_required = len(str(self.maximum))
        for digit_pos in range(digits_required):
            self.overwrite_range(0, self.n, self.counting_sort_internal(self.arr, digit_pos))
        self.green_ind = self.n - 1
        self.red_ind = self.n - 2

    def counting_sort(self):
        freqs = [0 for _ in range(self.maximum + 1)]
        for i in range(self.n):
            freqs[self.arr[i]] += 1
            self.green_ind = i
            self.wait()
        for i in range(1, self.maximum + 1):
            freqs[i] += freqs[i - 1]
            self.wait()
        for i in range(self.maximum - 1, -1, -1):
            freqs[i + 1] = freqs[i]
            freqs[i] = 0
            self.wait()
        result = [0 for _ in range(self.n)]
        for i in range(self.n):
            result[freqs[self.arr[i]]] = self.arr[i]
            freqs[self.arr[i]] += 1
            self.green_ind = i
            self.wait()
        self.overwrite_range(0, self.n, result)
        self.red_ind = self.n - 2

    def counting_sort_internal(self, array, digit_to_use):
        leny = len(array)
        maxy = 9
        freqs = [0 for _ in range(maxy + 1)]
        for i in range(leny):
            freqs[self.isolate_digit(array[i], digit_to_use)] += 1
            self.wait()
        for i in range(1, maxy + 1):
            freqs[i] += freqs[i - 1]
            self.wait()
        for i in range(maxy - 1, -1, -1):
            freqs[i + 1] = freqs[i]
            freqs[i] = 0
            self.wait()
        result = [0 for _ in range(leny)]
        for i in range(leny):
            result[freqs[self.isolate_digit(array[i], digit_to_use)]] = array[i]
            freqs[self.isolate_digit(array[i], digit_to_use)] += 1
            self.wait()
        return result

    def heap_sort(self):
        # self.overwrite_range(0, self.n, heapq._heapify_max(self.arr))
        # for i in range(self.n - 1, -1, -1):
        #     self.arr[i] = heapq._heappop_max(self.arr[:i+1])
        #     self.overwrite_range(0, i, heapq._heapify_max(self.arr[:i]))
        # Doesn't work
        heapq.heapify(self.arr)
        for i in range(self.n):
            self.wait()

        result = []
        for i in range(self.n):
            result.append(heapq.heappop(self.arr))
            self.arr.append(50)
            heapq.heapify(self.arr)
            self.green_ind = i
            self.wait()
        print(result)
        self.overwrite_range(0, self.n, result)
        self.green_ind = self.n - 1
        self.red_ind = self.n - 2

    # def bogo_sort(self):
    #     pass
