import React from 'react';
import { ArrowUpRight, ArrowDownRight, Activity } from 'lucide-react';

const NetworkChart = ({ networkData }) => {
    if (!networkData) return null;

    return (
        <div className="w-full min-h-[14rem] flex flex-col bg-zinc-900 rounded-xl p-4 border border-zinc-800">
            <div className="flex items-center gap-2 mb-4">
                <Activity className="w-4 h-4 text-emerald-500" />
                <h3 className="text-zinc-400 text-sm font-semibold">Speedtest & Usage</h3>
            </div>
            
            {/* Live Speeds */}
            <div className="flex flex-1 items-center justify-around mb-4">
                <div className="flex flex-col items-center">
                    <div className="w-12 h-12 rounded-full bg-blue-500/10 border border-blue-500/20 flex items-center justify-center mb-2 shadow-[0_0_15px_rgba(59,130,246,0.15)]">
                        <ArrowDownRight className="w-6 h-6 text-blue-400" />
                    </div>
                    <span className="text-2xl font-bold text-white tracking-tight">{networkData.download_speed || "0 Mbps"}</span>
                    <span className="text-[10px] text-blue-400/80 uppercase tracking-wider font-bold mt-1">Download</span>
                </div>
                
                <div className="w-px h-16 bg-zinc-800/50 mx-2"></div>
                
                <div className="flex flex-col items-center">
                    <div className="w-12 h-12 rounded-full bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center mb-2 shadow-[0_0_15px_rgba(16,185,129,0.15)]">
                        <ArrowUpRight className="w-6 h-6 text-emerald-400" />
                    </div>
                    <span className="text-2xl font-bold text-white tracking-tight">{networkData.upload_speed || "0 Mbps"}</span>
                    <span className="text-[10px] text-emerald-400/80 uppercase tracking-wider font-bold mt-1">Upload</span>
                </div>
            </div>
            
            {/* Cumulative Tags */}
            <div className="mt-auto flex flex-col gap-2">
                <div className="grid grid-cols-3 gap-2 text-xs">
                    <div className="bg-zinc-950/50 rounded-md p-2 border border-zinc-800/50 flex flex-col items-center justify-center">
                        <span className="text-zinc-500 text-[9px] uppercase font-semibold">Ping</span>
                        <span className="text-zinc-300 font-bold">{networkData.ping || "0 ms"}</span>
                    </div>
                    <div className="bg-zinc-950/50 rounded-md p-2 border border-zinc-800/50 flex flex-col items-center justify-center">
                        <span className="text-zinc-500 text-[9px] uppercase font-semibold">Downloaded</span>
                        <span className="text-zinc-300 font-medium">{networkData.total_downloaded}</span>
                    </div>
                    <div className="bg-zinc-950/50 rounded-md p-2 border border-zinc-800/50 flex flex-col items-center justify-center">
                        <span className="text-zinc-500 text-[9px] uppercase font-semibold">Uploaded</span>
                        <span className="text-zinc-300 font-medium">{networkData.total_uploaded}</span>
                    </div>
                </div>
                
                <div className="flex justify-between w-full text-[10px] text-zinc-600 px-1 mt-1">
                     <span>Pkts In: {networkData.packets_recv?.toLocaleString()}</span>
                     <span>Pkts Out: {networkData.packets_sent?.toLocaleString()}</span>
                </div>
            </div>
        </div>
    );
};

export default NetworkChart;
