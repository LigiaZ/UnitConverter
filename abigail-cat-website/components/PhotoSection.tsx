'use client';

import { useState, useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import { motion } from 'framer-motion';
import Image from 'next/image';

const PhotoSection = () => {
  const [uploadedImages, setUploadedImages] = useState<string[]>([]);

  const onDrop = useCallback((acceptedFiles: File[]) => {
    const newImages = acceptedFiles.map(file => URL.createObjectURL(file));
    setUploadedImages(prev => [...prev, ...newImages]);
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'image/*': ['.jpeg', '.jpg', '.png', '.gif']
    },
    multiple: true
  });

  return (
    <motion.section
      initial={{ opacity: 0, y: 50 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.8, delay: 0.2 }}
      className="py-12 px-4"
    >
      <div className="max-w-4xl mx-auto">
        <h2 className="text-4xl font-dancing-script text-white text-center mb-8">
          Abigail's Photos
        </h2>

        <div
          {...getRootProps()}
          className={`border-2 border-dashed rounded-lg p-8 text-center cursor-pointer transition-all duration-300 mb-8 ${
            isDragActive
              ? 'border-accent bg-accent/20 scale-105'
              : 'border-white/50 hover:border-accent hover:bg-white/10'
          }`}
        >
          <input {...getInputProps()} />
          <div className="text-white">
            {isDragActive ? (
              <p className="text-xl">Drop the photos here...</p>
            ) : (
              <p className="text-xl">
                Drag & drop photos of Abigail here, or click to select files
              </p>
            )}
          </div>
        </div>

        {uploadedImages.length > 0 && (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {uploadedImages.map((image, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, scale: 0.8 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
                className="relative group"
              >
                <div className="relative overflow-hidden rounded-lg shadow-lg hover:shadow-xl transition-shadow duration-300">
                  <Image
                    src={image}
                    alt={`Abigail photo ${index + 1}`}
                    width={400}
                    height={300}
                    className="w-full h-64 object-cover group-hover:scale-110 transition-transform duration-300"
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-black/50 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
                </div>
              </motion.div>
            ))}
          </div>
        )}
      </div>
    </motion.section>
  );
};

export default PhotoSection;