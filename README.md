# Activate conda
```bash
conda activate <condaenv>
```

# Install
```bash
uv pip install -e .
```

# Add new dependency
```bash
uv add <dependency>
```

# Sync package with system
```bash
uv pip sync --system ./pyproject.toml
```