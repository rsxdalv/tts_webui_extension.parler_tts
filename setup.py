import setuptools

setuptools.setup(
    name="extension_parler_tts",
    packages=setuptools.find_namespace_packages(),
    version="0.2.0",
    author="rsxdalv",
    description="Parler-TTS is a training and inference library for high-fidelity text-to-speech (TTS) models.",
    url="https://github.com/rsxdalv/extension_parler_tts",
    project_urls={},
    scripts=[],
    install_requires=[
        "parler-tts @ git+https://github.com/huggingface/parler-tts@main",
        # "transformers==4.43.3",
        # "numpy==1.24.4",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
