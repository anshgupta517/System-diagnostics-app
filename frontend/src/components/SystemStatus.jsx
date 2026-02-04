import React from 'react';
import { Activity } from 'lucide-react';

const SystemStatus = ({ status }) => {
    const isOnline = status === 'System Summarizer Backend Running';

    return (
        <div className={`inline-flex items-center gap-2 px-3 py-1.5 rounded-full text-xs font-medium border ${isOnline
                ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20'
                : 'bg-red-500/10 text-red-400 border-red-500/20'
            }`}>
            <Activity className="w-3.5 h-3.5" />
            <span>{isOnline ? 'System Online' : 'Connecting...'}</span>
        </div>
    );
};

export default SystemStatus;
