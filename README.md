# Embedding Server

High-throughput embedding server supporting Sentence Transformers.

## Features
- OpenAI-compatible /v1/embeddings endpoint
- Dynamic batching with configurable max batch size
- Model hot-swapping without restart
- FP16 inference with automatic precision

## Performance
| Model | Throughput | Latency (p99) |
|-------|-----------|---------------|
| all-MiniLM-L6-v2 | 12K req/s | 8ms |
| BGE-large-en | 4.2K req/s | 24ms |

## License
MIT
