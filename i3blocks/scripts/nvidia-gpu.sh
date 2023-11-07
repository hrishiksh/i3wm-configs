#!/bin/bash

GPU_UTILIZATION=$(nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader)
# GPU_MEMORY=$(nvidia-smi --query-gpu=utilization.memory --format=csv,noheader)
# GPU_TEMPERATURE=$(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader)
# GPU_POWER=$(nvidia-smi --query-gpu=power.draw --format=csv,noheader)

echo "${GPU_UTILIZATION}"
