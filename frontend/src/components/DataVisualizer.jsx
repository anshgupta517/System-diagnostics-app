import React from 'react';
import CpuChart from './charts/CpuChart';
import MemoryChart from './charts/MemoryChart';
import ProcessChart from './charts/ProcessChart';

const DataVisualizer = ({ data }) => {
    if (!data) return null;

    return (
        <div className="mt-4 flex flex-col gap-4 w-full">
            <div className="flex flex-col sm:flex-row gap-4 w-full justify-between">
                {data.get_cpu_stats && (
                    <div className="flex-1 min-w-[200px]">
                         <CpuChart cpuData={data.get_cpu_stats} />
                    </div>
                )}
                
                {data.get_memory_stats && (
                    <div className="flex-1 min-w-[200px]">
                         <MemoryChart memoryData={data.get_memory_stats} />
                    </div>
                )}
            </div>
            
            {data.get_process_list && (
                 <div className="w-full">
                      <ProcessChart processData={data.get_process_list} />
                 </div>
            )}
        </div>
    );
};

export default DataVisualizer;
