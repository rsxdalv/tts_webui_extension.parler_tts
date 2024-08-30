import setuptools

setuptools.setup(
    name="extension_parler_tts",
    packages=setuptools.find_namespace_packages(),
    version="0.0.1",
    author="rsxdalv",
    description="Parler TTS",
    url="https://github.com/rsxdalv/extension_parler_tts",
    project_urls={},
    scripts=[],
    install_requires=[
        "git+https://github.com/huggingface/parler-tts.git",
        # "transformers==4.43.3",
        # "numpy==1.24.4",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
